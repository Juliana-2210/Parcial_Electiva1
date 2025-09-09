import os
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer


pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("articulos-cientificos")  

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

pregunta = "avances recientes en inteligencia artificial aplicada a la medicina"


vector_pregunta = model.encode(pregunta).tolist()


resultado = index.query(
    vector=vector_pregunta,
    top_k=5,  
    include_metadata=True
)


print("\n🔎 Resultados más relevantes:\n")
for match in resultado["matches"]:
    print(f"ID: {match['id']}")
    print(f"Título: {match['metadata'].get('titulo', 'N/A')}")
    print(f"Resumen: {match['metadata'].get('resumen', 'N/A')[:200]}...")
    print(f"Score de similitud: {match['score']:.4f}\n")
