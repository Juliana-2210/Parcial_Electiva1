import os
from dotenv import load_dotenv
from pathlib import Path

# forzar a cargar el .env en la raíz del proyecto
dotenv_path = Path(__file__).resolve().parent / ".env"
print("Buscando .env en:", dotenv_path)

load_dotenv(dotenv_path=dotenv_path)

print("API KEY:", os.getenv("PINECONE_API_KEY"))
print("ENV:", os.getenv("PINECONE_ENV"))
print("INDEX:", os.getenv("PINECONE_INDEX"))
