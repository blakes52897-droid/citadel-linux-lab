import os
import sys
import requests
import chromadb

ROOT_DIR = os.path.expanduser("~/citadel-linux-lab")
DB_DIR = os.path.join(ROOT_DIR, "rag", "vector-db")

OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"
OLLAMA_CHAT_URL = "http://localhost:11434/api/generate"

EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "llama3.2:3b"

client = chromadb.PersistentClient(path=DB_DIR)

collection = client.get_or_create_collection(
    name="citadel_knowledge"
)


def embed_text(text):
    response = requests.post(
        OLLAMA_EMBED_URL,
        json={
            "model": EMBED_MODEL,
            "prompt": text
        },
        timeout=60
    )

    response.raise_for_status()
    return response.json()["embedding"]


def ask_llm(question, context):
    prompt = f"""
You are Odysseus, the AI Operations Assistant for The Citadel.

Answer the user's question using only the Citadel context below.
If the answer is not in the context, say what is missing instead of guessing.

CITADEL CONTEXT:
{context}

USER QUESTION:
{question}

Do not use hidden reasoning. Do not think silently. Answer directly in 1-2 short paragraphs.


ANSWER:
"""

    response = requests.post(
        OLLAMA_CHAT_URL,
        json={
    "model": CHAT_MODEL,
    "prompt": prompt,
    "stream": False,
    "keep_alive": "30m",
    "options": {
        "num_predict": 180,
        "temperature": 0.2,
        "num_thread": 4
    }
},
        timeout=600
    )

    response.raise_for_status()
    return response.json()["response"]


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 rag/query.py "What is The Citadel project?"')
        return

    question = " ".join(sys.argv[1:])

    question_embedding = embed_text(question)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=2
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        print("No relevant Citadel context found. Run ingest.py first.")
        return

    context_blocks = []

    for doc, metadata in zip(documents, metadatas):
        source = metadata.get("source", "unknown")
        chunk = metadata.get("chunk", "unknown")

        context_blocks.append(
            f"Source: {source}, chunk {chunk}\n{doc}"
        )

    context = "\n\n---\n\n".join(context_blocks)

    print("\nRetrieved Citadel context:")
    for metadata in metadatas:
        print(f"- {metadata.get('source')} chunk {metadata.get('chunk')}")

    print("\nOdysseus answer:\n")
    answer = ask_llm(question, context)
    print(answer)


if __name__ == "__main__":
    main()
