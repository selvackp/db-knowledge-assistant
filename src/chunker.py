def chunk_text(text, chunk_size=2000):
    """
    Split text into chunks for vector indexing.
    Larger chunk size reduces total embeddings
    and improves ingestion performance.
    """

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]

        if chunk.strip():
            chunks.append(chunk)

    return chunks
