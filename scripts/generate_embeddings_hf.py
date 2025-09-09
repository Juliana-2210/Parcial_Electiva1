
import os
import json
from pathlib import Path
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

RAW_FILE = Path("data/raw/raw_articles.jsonl")
OUT_FILE = Path("data/embeddings/embeddings.jsonl")

OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

def main():
    if not RAW_FILE.exists():
        print(f" No existe el archivo {RAW_FILE}. Primero ejecuta extract_text.py")
        return

    print("📥 Cargando modelo de Hugging Face (all-MiniLM-L6-v2)...")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    docs = []
    with RAW_FILE.open("r", encoding="utf-8") as fin:
        for line in fin:
            try:
                docs.append(json.loads(line))
            except Exception as e:
                print(" Error leyendo línea:", e)

    print(f"📄 Documentos cargados: {len(docs)}")
    if not docs:
        print(" No hay documentos en el archivo raw_articles.jsonl")
        return

    with OUT_FILE.open("w", encoding="utf-8") as fout:
        for doc in tqdm(docs, desc="Generando embeddings"):
            body = doc.get("body", "").strip()
            if not body:
                print(f" Documento {doc.get('id')} vacío, lo salto")
                continue

            
            embedding = model.encode(body).tolist()

         
            out_doc = {
                "id": doc.get("id"),
                "title": doc.get("title"),
                "body": body[:200], 
                "embedding": embedding
            }
            fout.write(json.dumps(out_doc, ensure_ascii=False) + "\n")

    print(f" Embeddings generados en {OUT_FILE}")

if __name__ == "__main__":
    main()
