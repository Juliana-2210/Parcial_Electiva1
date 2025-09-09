from pinecone import Pinecone, ServerlessSpec
import os

api_key = "pcsk_4UH7i5_TBSE3RCzvLJbC6a4cLvhHragBmRdUC8ULP9uDt8iB3cBtgDJeSqYVFuPU9HQboY"  


index_name = "demo-index"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=128,  
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

print("Índice creado correctamente ")
