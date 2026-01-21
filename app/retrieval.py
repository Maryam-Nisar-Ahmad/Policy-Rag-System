import os
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Model
_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


#config
top_k = 5
storage_dir = "storage"


def load_store():
    embeddings_path = os.path.join(storage_dir, "embeddings.npy")
    docs_path = os.path.join(storage_dir, "documents.pkl")

    #index not built yet→ return empty
    if not os.path.exists(embeddings_path) or not os.path.exists(docs_path):
        return None, None

    embeddings = np.load(embeddings_path)

    with open(docs_path, "rb") as f:
        documents = pickle.load(f)

    return embeddings, documents


def search_docs(query, min_score=0.20):
    embeddings, documents = load_store()

    # no index → no results
    if embeddings is None or documents is None:
        return []

    model = get_model()
    query_vector = model.encode([query])

    scores = cosine_similarity(query_vector, embeddings)[0]

    top_indices = scores.argsort()[-top_k:][::-1]

    results = []
    for i in top_indices:
        if scores[i] >= min_score:
            results.append(documents[i])

    return results
