import os

# Absolute base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Embedding model (single source of truth)
embedding_model = "all-MiniLM-L6-v2"

# Data & storage paths (ABSOLUTE)
data_dir = os.path.join(BASE_DIR, "data")
storage_dir = os.path.join(BASE_DIR, "storage")
docs_path = os.path.join(storage_dir, "documents.pkl")

# Chunking
chunk_size = 500
chunk_overlap = 100

# Retrieval
top_k = 5
