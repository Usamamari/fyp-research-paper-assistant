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
    # handle empty input
    if not query.strip():
        return "Please enter a valid question related to the research papers."

    # handle system-related questions
    if "llm" in query.lower() or "model" in query.lower():
        return (
            "The system uses a transformer-based language model (DistilBERT) "
            "to perform document-grounded question answering."
        )

    # embed query
    query_embedding = embedder.encode([query]).astype("float32")
    _, indices = index.search(query_embedding, k=2)

    # build context
    context = " ".join([documents[i] for i in indices[0]])
    context = context[:3000]

    # run QA
    result = qa_model(
        question=query,
        context=context
    )

    answer = result.get("answer", "").strip()

    if answer == "":
        return (
            "No relevant information was found in the uploaded research papers. "
            "Please ask a question directly related to the document content."
        )

    return answer
