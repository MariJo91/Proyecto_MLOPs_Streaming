# Sistema de Recomendacion basado en Machine Learning

# Implementacion del Modelo de Recomendacion, obtando por un filtrado basado en contenido. Este enfoque nos permitirá recomendar películas similares basadas en características como actores, directores y género.

# Preparamos el Entorno e Instalamos las Bibliotecas necesarias

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd

# Definir el modelo para la respuesta de la API
class RecommendationResponse(BaseModel):
    title: str
    genre: str
    movie_id: int

# Cargamos los dataset necesarios

generos = pd.read_parquet('DataSets_Clean/df_genres_limpio.parquet')
peliculas = pd.read_parquet('DataSets_Clean/df_movies_limpio.parquet')

# Renombrar columnas para la fusión

generos.rename(columns={'id': 'movie_id'}, inplace=True)
peliculas.rename(columns={'id': 'movie_id'}, inplace=True)

# Fusionar los datasets
data = peliculas.merge(generos, on='movie_id', how='left')

# Función de recomendación
def recomendar_pelicula_por_genero(genero: str, n_recomendaciones: int = 5) -> List[RecommendationResponse]:
    # Normalizar el género de entrada
    genero_normalizado = genero.lower().strip()

    # Filtrar películas por género
    recomendaciones = data[data['name'].str.lower() == genero_normalizado]

    # Seleccionar las mejores n recomendaciones
    recomendaciones_top = recomendaciones[['title', 'name', 'movie_id']].head(n_recomendaciones)

    # Convertir a lista de objetos RecommendationResponse
    return [RecommendationResponse(title=row['title'], genre=row['name'], movie_id=row['movie_id']) for index, row in recomendaciones_top.iterrows()]