import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader

PDF_PATH = "data/research papers"
OUT_DIR = "vector_store"
os.makedirs(OUT_DIR, exist_ok=True)

documents = []

for file in os.listdir(PDF_PATH):
    if file.endswith(".pdf"):
        reader = PdfReader(os.path.join(PDF_PATH, file))
        for page in reader.pages:
            text = page.extract_text()
            if text:
                documents.append(text)

print(f"Total pages loaded: {len(documents)}")

# Embeddings (FREE)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embeddings = model.encode(documents, show_progress_bar=True).astype("float32")

# FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, f"{OUT_DIR}/faiss.index")

with open(f"{OUT_DIR}/docs.pkl", "wb") as f:
    pickle.dump(documents, f)

print("✅ Vector store created (FREE, no API)")
