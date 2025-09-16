from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

# Inicializar modelos
sentiment_model = pipeline("sentiment-analysis")
keyword_model = KeyBERT()
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Pedir texto por consola
text = input("Escribe un comentario: ")

# 1. Análisis de sentimiento
sentiment = sentiment_model(text)[0]

# 2. Palabras clave
keywords = keyword_model.extract_keywords(text, top_n=5)
keywords = [kw[0] for kw in keywords]

# 3. Embedding
embedding = embedding_model.encode(text).tolist()

# Mostrar resultados
print("\n--- Resultados ---")
print("Sentimiento:", sentiment)
print("Palabras clave:", keywords)
print("Embedding (primeros 10 valores):", embedding[:10])
