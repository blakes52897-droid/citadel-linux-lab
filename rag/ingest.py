import os
import requests
import chromadb

ROOT_DIR = os.path.expanduser("~/citadel-linux-lab")
DB_DIR = os.path.join(ROOT_DIR, "rag", "vector-db")

SOURCE_PATHS = [
    "README.md",
    "notes",
    "docs",
    "docker-site/projects",
]

OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"

client = chromadb.PersistentClient(path=DB_DIR)

collection = client.get_or_create_collection(
    name="citadel_knowledge"
)


def read_text_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            return file.read()
    except Exception as error:
        print(f"Could not read {path}: {error}")
        return ""


def chunk_text(text, chunk_size=900, overlap=150):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


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


def collect_files():
    files = []

    for source in SOURCE_PATHS:
        full_path = os.path.join(ROOT_DIR, source)

        if os.path.isfile(full_path):
            files.append(full_path)

        if os.path.isdir(full_path):
            for dirpath, _, filenames in os.walk(full_path):
                for filename in filenames:
                    if filename.endswith((".md", ".txt", ".html")):
                        files.append(os.path.join(dirpath, filename))

    return files


def main():
    files = collect_files()

    if not files:
        print("No source files found.")
        return

    print(f"Found {len(files)} source files.")

    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for file_path in files:
        rel_path = os.path.relpath(file_path, ROOT_DIR)
        text = read_text_file(file_path)
        chunks = chunk_text(text)

        print(f"Ingesting {rel_path}: {len(chunks)} chunks")

        for index, chunk in enumerate(chunks):
            chunk_id = f"{rel_path}-{index}"

            try:
                embedding = embed_text(chunk)
            except Exception as error:
                print(f"Embedding failed for {chunk_id}: {error}")
                continue

            ids.append(chunk_id)
            documents.append(chunk)
            embeddings.append(embedding)
            metadatas.append({
                "source": rel_path,
                "chunk": index
            })

    if ids:
        collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    print(f"Done. Stored {len(ids)} chunks in Odysseus Memory Core.")


if __name__ == "__main__":
    main()
