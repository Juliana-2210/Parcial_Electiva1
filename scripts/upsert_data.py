from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
import os


pinecone_api_key = os.getenv("PINECONE_API_KEY", "pcsk_4UH7i5_TBSE3RCzvLJbC6a4cLvhHragBmRdUC8ULP9uDt8iB3cBtgDJeSqYVFuPU9HQboY")
index_name = "articulos-cientificos"

pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index(index_name)


model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")  


texts = [
    {"id": "vec1", "texto": "Hola mundo"},
    {"id": "vec2", "texto": "Base de datos vectorial"},
    {"id": "vec3", "texto": "Pinecone con Python"}
]

vectors = []


for item in texts:
    vector_values = model.encode(item["texto"]).tolist() 
    vectors.append({
        "id": item["id"],
        "values": vector_values,
        "metadata": {"texto": item["texto"]}
    })


index.upsert(vectors=vectors)

print("Vectores insertados correctamente en Pinecone")
