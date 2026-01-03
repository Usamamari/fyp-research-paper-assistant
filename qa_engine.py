import faiss
import pickle
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# ---------------- PATHS ----------------
VECTOR_DB_PATH = "vector_store/faiss.index"
DOC_STORE_PATH = "vector_store/docs.pkl"

# ---------------- LOAD MODELS ----------------
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

index = faiss.read_index(VECTOR_DB_PATH)

with open(DOC_STORE_PATH, "rb") as f:
    documents = pickle.load(f)

qa_model = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad",
    device=-1
)

# ---------------- MAIN FUNCTION ----------------
def ask_question(query: str) -> str:
    if not query.strip():
        return "Please enter a valid question."

    query_embedding = embedder.encode([query]).astype("float32")
    _, indices = index.search(query_embedding, k=2)

    context = " ".join([documents[i] for i in indices[0]])
    context = context[:3000]

    result = qa_model(
        question=query,
        context=context
    )

    return result["answer"]
