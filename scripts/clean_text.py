
import json
import re
from pathlib import Path
from tqdm import tqdm

IN_FILE = Path("data/raw/raw_articles.jsonl")
OUT_FILE = Path("data/clean/clean_articles.jsonl")
OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

def clean_text(text: str) -> str:
    if not text:
        return ""
    txt = re.sub(r'\r\n', '\n', text)
    txt = re.sub(r'\n{2,}', '\n\n', txt)
    txt = re.sub(r'[ \t]{2,}', ' ', txt)
    lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
    filtered = [ln for ln in lines if len(ln) > 2]
    cleaned = "\n".join(filtered)
    return cleaned.strip()

def main():
    with IN_FILE.open("r", encoding="utf-8") as fin, OUT_FILE.open("w", encoding="utf-8") as fout:
        for line in tqdm(fin, desc="Limpiando artículos"):
            doc = json.loads(line)
            doc["body"] = clean_text(doc.get("body", ""))
      
            doc["title"] = re.sub(r'\s+', ' ', (doc.get("title") or "")).strip()
            fout.write(json.dumps(doc, ensure_ascii=False) + "\n")
    print("Limpieza completada ->", OUT_FILE)

if __name__ == "__main__":
    main()
