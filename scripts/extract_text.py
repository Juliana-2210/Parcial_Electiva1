# scripts/extract_text.py
import os
import json
import pdfplumber
from dotenv import load_dotenv
from pathlib import Path
from tqdm import tqdm

load_dotenv()

PDF_DIR = Path("data/pdfs")
OUT_FILE = Path("data/raw/raw_articles.jsonl")

OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

def extract_text_from_pdf(path: Path) -> dict:
    text_pages = []
    title = None
    try:
        with pdfplumber.open(path) as pdf:
            # metadata title si existe
            meta = pdf.metadata or {}
            title = meta.get("Title") or meta.get("title")
            for p in pdf.pages:
                txt = p.extract_text()
                if txt:
                    text_pages.append(txt)
    except Exception as e:
        print(f"Error leyendo {path}: {e}")
        return None

    full_text = "\n".join(text_pages).strip()
    # si no se obtuvo título, toma primera línea del texto
    if not title and full_text:
        first_line = next((ln.strip() for ln in full_text.splitlines() if ln.strip()), "")
        title = first_line[:200] if first_line else path.stem

    return {
        "id": path.stem,
        "filename": str(path.name),
        "title": title or path.stem,
        "body": full_text
    }

def main():
    files = sorted(PDF_DIR.glob("*.pdf"))
    with OUT_FILE.open("w", encoding="utf-8") as fout:
        for f in tqdm(files, desc="Extrayendo PDFs"):
            doc = extract_text_from_pdf(f)
            if doc:
                fout.write(json.dumps(doc, ensure_ascii=False) + "\n")
    print("Extracción finalizada ->", OUT_FILE)

if __name__ == "__main__":
    main()
