import valkey
import numpy as np
from sentence_transformers import SentenceTransformer
from src.config import *

client = valkey.Valkey(
    host=MEMORYDB_HOST,
    port=MEMORYDB_PORT,
    username=MEMORYDB_USER,
    password=MEMORYDB_PASSWORD,
    ssl=True
)

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def search_documents(question):

    query_vector = model.encode(
        question
    )

    results = client.execute_command(
        "FT.SEARCH",
        "docs_idx",
        "*=>[KNN 5 @embedding $vec]",
        "PARAMS",
        2,
        "vec",
        np.array(
            query_vector,
            dtype=np.float32
        ).tobytes(),
        "SORTBY",
        "__embedding_score",
        "RETURN",
        2,
        "document",
        "chunk",
        "DIALECT",
        2
    )

    return results
