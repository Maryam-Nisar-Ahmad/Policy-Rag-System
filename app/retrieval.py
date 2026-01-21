import os
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from app.settings import storage_dir, docs_path, embedding_model, top_k

# Singleton model (load once)
_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(embedding_model)
    return _model


def load_store():
    embeddings_path = os.path.join(storage_dir, "embeddings.npy")

    # Index not built yet
    if not os.path.exists(embeddings_path) or not os.path.exists(docs_path):
        return None, None

    embeddings = np.load(embeddings_path)

    with open(docs_path, "rb") as f:
        documents = pickle.load(f)

    return embeddings, documents


def search_docs(query):
    embeddings, documents = load_store()

    # No index → no results
    if embeddings is None or documents is None:
        return []

    model = get_model()
    query_vector = model.encode([query])

    scores = cosine_similarity(query_vector, embeddings)[0]

    # Always take top-k (NO hard cutoff)
    top_indices = scores.argsort()[-top_k:][::-1]

    results = [documents[i] for i in top_indices]

    return results
