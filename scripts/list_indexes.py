from pinecone import Pinecone
import os

api_key = os.getenv("PINECONE_API_KEY", "pcsk_4UH7i5_TBSE3RCzvLJbC6a4cLvhHragBmRdUC8ULP9uDt8iB3cBtgDJeSqYVFuPU9HQboY")
pc = Pinecone(api_key=api_key)

print("📂 Índices disponibles en tu cuenta:")
print(pc.list_indexes())
