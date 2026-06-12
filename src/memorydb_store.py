import valkey
import numpy as np
from src.config import *

client = valkey.Valkey(
    host=MEMORYDB_HOST,
    port=MEMORYDB_PORT,
    username=MEMORYDB_USER,
    password=MEMORYDB_PASSWORD,
    ssl=True
)


def store_chunk(
        document_name,
        chunk_id,
        text,
        embedding):

    key = f"doc:{document_name}:{chunk_id}"

    client.hset(
        key,
        mapping={
            "document": document_name,
            "chunk": text,
            "embedding": np.array(
                embedding,
                dtype=np.float32
            ).tobytes()
        }
    )


def document_exists(document_name):

    return client.sismember(
        "documents",
        document_name
    )


def register_document(document_name):

    client.sadd(
        "documents",
        document_name
    )


def get_documents():

    docs = client.smembers(
        "documents"
    )

    return sorted(
        [d.decode()
         if isinstance(d, bytes)
         else d
         for d in docs]
    )
