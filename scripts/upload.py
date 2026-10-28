"""Create the benchmark collection and upload data/chunks.jsonl with Cloud Inference.

    python -I scripts/upload.py create    # collection + payload indexes, indexing paused
    python -I scripts/upload.py upload    # resumable; embeds server-side with MiniLM
    python -I scripts/upload.py index     # resume HNSW indexing and wait for green

Collection layout for a 1 vCPU / ~1.8 GB RAM cluster: original vectors on disk, int8
scalar quantization in RAM (rescored from disk), payload on disk, HNSW m=16,
ef_construct=100. Indexing is paused during the bulk upload and resumed afterwards.
"""
import json
import pathlib
import sys
import time
from concurrent.futures import ThreadPoolExecutor

from qdrant_client import models

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from qdrant_conn import COLLECTION, DIM, MODEL, client  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHUNKS, PROGRESS = ROOT / "data" / "chunks.jsonl", ROOT / "data" / "upload_progress.json"
BATCH, WORKERS = 256, 4


def create():
    c = client()
    if c.collection_exists(COLLECTION):
        print("exists:", COLLECTION)
        return
    c.create_collection(
        COLLECTION,
        vectors_config=models.VectorParams(size=DIM, distance=models.Distance.COSINE, on_disk=True),
        quantization_config=models.ScalarQuantization(scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8, quantile=0.99, always_ram=True)),
        hnsw_config=models.HnswConfigDiff(m=16, ef_construct=100),
        optimizers_config=models.OptimizersConfigDiff(indexing_threshold=0),
        on_disk_payload=True,
    )
    c.create_payload_index(COLLECTION, "site", models.PayloadSchemaType.KEYWORD)
    c.create_payload_index(COLLECTION, "thread", models.PayloadSchemaType.INTEGER)
    c.create_payload_index(COLLECTION, "post", models.PayloadSchemaType.INTEGER)   # used by open()
    print("created", COLLECTION)


def batches(start):
    batch = []
    for line in open(CHUNKS, encoding="utf-8"):
        r = json.loads(line)
        if r["id"] < start:
            continue
        batch.append(r)
        if len(batch) == BATCH:
            yield batch
            batch = []
    if batch:
        yield batch


def send(c, batch):
    pts = [models.PointStruct(id=r["id"], vector=models.Document(text=r["text"], model=MODEL),
                              payload={k: r[k] for k in ("site", "thread", "post", "chunk", "n_chunks",
                                                         "score", "accepted", "title", "text")})
           for r in batch]
    for attempt in range(8):
        try:
            c.upsert(COLLECTION, points=pts, wait=False)
            return batch[-1]["id"]
        except Exception as e:  # network or rate limit: back off and retry the same batch
            time.sleep(min(60, 2 ** attempt))
            err = e
    raise RuntimeError(f"batch at id {batch[0]['id']} failed: {err}")


def upload():
    c = client(timeout=300)
    start = json.load(open(PROGRESS))["next"] if PROGRESS.exists() else 0
    t0, done = time.time(), 0
    with ThreadPoolExecutor(WORKERS) as pool:
        window = []
        for batch in batches(start):
            window.append(pool.submit(send, c, batch))
            if len(window) == WORKERS * 4:
                last = max(f.result() for f in window)
                done += sum(1 for _ in window) * BATCH
                window = []
                json.dump({"next": last + 1}, open(PROGRESS, "w"))
                rate = done / (time.time() - t0)
                print(f"next id {last + 1}, {rate:.0f} points/s", flush=True)
        if window:
            last = max(f.result() for f in window)
            json.dump({"next": last + 1}, open(PROGRESS, "w"))
    print("upload finished; points:", c.count(COLLECTION, exact=True).count)


def index():
    c = client()
    c.update_collection(COLLECTION, optimizers_config=models.OptimizersConfigDiff(indexing_threshold=20000))
    while True:
        info = c.get_collection(COLLECTION)
        print(f"status {info.status}, points {info.points_count}, indexed {info.indexed_vectors_count}", flush=True)
        if info.status == models.CollectionStatus.GREEN and info.indexed_vectors_count >= 0.99 * (info.points_count or 1):
            break
        time.sleep(60)


if __name__ == "__main__":
    {"create": create, "upload": upload, "index": index}[sys.argv[1]]()
