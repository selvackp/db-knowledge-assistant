from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def generate_embeddings(chunks):

    embeddings = model.encode(
        chunks,
        batch_size=64,
        show_progress_bar=False
    )

    return embeddings
