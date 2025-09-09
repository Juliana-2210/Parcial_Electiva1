#  Proyecto Parcial Electiva 1 – Pinecone y Embeddings

Este proyecto corresponde al **Parcial de la materia Electiva 1**, en el cual se implementa el uso de **vectores y consultas semánticas** utilizando **Pinecone** como base de datos vectorial.


##  Objetivo
Implementar un flujo de trabajo donde:
1. Se crea un índice en **Pinecone**.  
2. Se generan embeddings a partir de documentos.  
3. Se insertan (upsert) los vectores en el índice.  
4. Se consulta la base vectorial para recuperar información similar.  

---

##  Pasos realizados

1. **Instalación de dependencias**  
   
   pip install pinecone-client
   pip install python-dotenv
   pip install transformers
Configuración de entorno

Creación de archivo .env con la API Key de Pinecone:

PINECONE_API_KEY=tu_api_key_aqui
Creación del índice en Pinecone

Dimensión: 768

Métrica: cosine

Carga de datos y generación de embeddings

Se descargaron artículos de prueba en la carpeta /data

Se generaron embeddings usando HuggingFace (all-MiniLM-L6-v2)

Se insertaron en el índice (upsert)

Consulta de datos (query)

Se realizó una búsqueda vectorial a Pinecone

Se obtuvieron los resultados con mayor similitud

 Estructura del proyecto

Parcial_Electiva1/
│── data/                  # Documentos de prueba
│── scripts/               # Scripts principales
│   ├── create_index.py    # Crear índice en Pinecone
│   ├── upsert_data.py     # Insertar embeddings
│   ├── query_data.py      # Consultar índice
│── .env                   # Variables de entorno (no subir a GitHub)
│── requirements.txt       # Dependencias
│── README.md              # Documentación del proyecto

▶Cómo ejecutar:

Clonar el repositorio:

git clone https://github.com/Juliana-2210/Parcial_Electiva1.git
cd Parcial_Electiva1

Instalar dependencias:

pip install -r requirements.txt

Configurar tu .env con tu API Key.

Ejecutar scripts en orden:

python scripts/create_index.py

python scripts/upsert_data.py

python scripts/query_data.py

 Evidencias:
 
Creación y estado del índice en Pinecone

Inserción de 3 vectores

Consulta con resultados de similitud

 Autor: Juliana Rincón
UPTC – Electiva 1 – 2025
