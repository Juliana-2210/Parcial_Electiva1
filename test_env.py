import os
from dotenv import load_dotenv
import pinecone


load_dotenv()

pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENV")
pinecone_index = os.getenv("PINECONE_INDEX")

print(" Clave Pinecone:", pinecone_api_key[:8] + "..." if pinecone_api_key else "No encontrada")
print(" Entorno:", pinecone_env)
print(" Nombre del índice:", pinecone_index)

pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)

print("📊 Índices disponibles:", pinecone.list_indexes())
