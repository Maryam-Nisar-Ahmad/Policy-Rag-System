import os
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

from app.settings import (
    data_dir,
    storage_dir,
    docs_path,
    embedding_model,
    chunk_size,
    chunk_overlap,
)

def split_text(text, size, overlap):
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i : i + size])
        i += size - overlap
    return chunks


def load_documents():
    documents = []

    for filename in os.listdir(data_dir):
        if not filename.endswith(".txt"):
            continue

        path = os.path.join(data_dir, filename)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        parts = split_text(text, chunk_size, chunk_overlap)

        for part in parts:
            documents.append({
                "content": part,
                "source": filename
            })

    return documents


def build_index():
    documents = load_documents()
    texts = [d["content"] for d in documents]

    if not texts:
        return 0

    model = SentenceTransformer(embedding_model)
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings)

    os.makedirs(storage_dir, exist_ok=True)

    np.save(os.path.join(storage_dir, "embeddings.npy"), embeddings)

    with open(docs_path, "wb") as f:
        pickle.dump(documents, f)

    return len(documents)
