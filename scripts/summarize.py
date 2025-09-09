
import os
import json
import argparse
import re
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

IN_FILE = Path("data/clean/clean_articles.jsonl")
OUT_CSV = Path("data/summaries/summaries.csv")
OUT_CSV.parent.mkdir(parents=True, exist_ok=True)

def heuristic_summary(text, n_sentences=3):
   
    sents = re.split(r'(?<=[.!?])\s+', text)
    return " ".join(sents[:n_sentences]).strip()

def openai_summarize(text, max_words=120):
    try:
        import openai
        openai.api_key = OPENAI_API_KEY
    except Exception as e:
        raise RuntimeError("openai no disponible o no instalado") from e

    prompt = (
        "Resume en un solo párrafo (máx. {} palabras) el siguiente texto académico. "
        "Mantén el tono formal y conserva términos técnicos importantes.\n\n"
        "TEXTO:\n{}"
    ).format(max_words, text[:3000])  
    
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente que resume artículos científicos."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.0
    )
    return resp["choices"][0]["message"]["content"].strip()

def main(method="heuristic"):
    rows = []
    with IN_FILE.open("r", encoding="utf-8") as fin:
        for line in tqdm(fin, desc="Generando resúmenes"):
            doc = json.loads(line)
            body = doc.get("body", "")
            if not body:
                resumen = ""
            else:
                try:
                    if method == "heuristic":
                        resumen = heuristic_summary(body, n_sentences=3)
                    elif method == "openai":
                        resumen = openai_summarize(body, max_words=140)
                    else:
                        raise ValueError("Método desconocido")
                except Exception as e:
                    print("Error resumen para", doc.get("id"), e)
                    resumen = heuristic_summary(body, n_sentences=2)
            rows.append({
                "id": doc.get("id"),
                "titulo": doc.get("title"),
                "resumen": resumen
            })
    df = pd.DataFrame(rows)
    df.to_csv(OUT_CSV, index=False)
    print("Resúmenes guardados ->", OUT_CSV)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", choices=["heuristic", "openai"], default="heuristic")
    args = parser.parse_args()
    main(method=args.method)
