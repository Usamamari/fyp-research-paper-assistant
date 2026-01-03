import os
from langchain_community.document_loaders import PyPDFLoader


PDF_PATH = "data/research papers"


all_docs = []

for file in os.listdir(PDF_PATH):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(PDF_PATH, file))
        docs = loader.load()
        all_docs.extend(docs)

print(f"Total pages loaded: {len(all_docs)}")
