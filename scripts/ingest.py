import os

from src.pdf_loader import extract_text
from src.chunker import chunk_text
from src.embeddings import generate_embedding
from src.valkey_store import save_chunk

folder = "documents"

for file in os.listdir(folder):

    if file.endswith(".pdf"):

        path = os.path.join(folder, file)

        text = extract_text(path)

        chunks = chunk_text(text)

        for idx, chunk in enumerate(chunks):

            embedding = generate_embedding(chunk)

            save_chunk(
                f"{file}_{idx}",
                chunk,
                embedding
            )

print("Completed")
