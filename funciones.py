
from fastapi import FastAPI, HTTPException
import pandas as pd
import pyarrow.parquet as pq


# Carga del dataset / Conjunto de Datos

# Crear una lista para almacenar los DataFrames
dfs = []

# Iterar sobre los archivos Parquet y leerlos
for archivo in ['DataSets/df_companies_limpio.parquet', 'DataSets/df_credits_limpio.parquet', 'DataSets/df_genres_limpio.parquet', 'DataSets/df_movies_limpio.parquet']:
    data_total = pq.read_table(archivo).to_pandas()
    dfs.append(data_total)

    # Concatenar todos los DataFrames en uno solo
    data_total = pd.concat(dfs)

# Nos aseguramos que la columna 'fecha_de_estreno' sea de tipo datetime
data_total["release_date"] = pd.to_datetime(data_total["release_date"])

# Verificamos si hay fechas validas
if data_total["release_date"].isnull().any():
    print("Hay fechas no válidas en el DataFrame")



# 1. Funcion Cantidad de Filmaciones por Mes ____________________________________________________________________________________________________________________________

def cantidad_filmaciones_mes(nombre_mes: str) -> int:
    meses = {
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12
    }

    mes = meses.get(nombre_mes.lower())

    if mes is None:
        return 0  # Retorna 0 si el mes no es válido

    data_total["release_date"] = pd.to_datetime(data_total["release_date"])
    return data_total[data_total["release_date"].dt.month == mes].shape[0]



# 2. Funcion Cantidad de Filmaciones por Dia _____________________________________________________________________________________________________________________________

def cantidad_filmaciones_por_fecha_dia(fecha_dia: str) -> int:
    try:
        # Convertir la fecha de string a datetime
        fecha_obj = pd.to_datetime(fecha_dia, format='%d-%m-%Y', errors='raise')
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de fecha no válido. Use DD-MM-YYYY.")

    # Filtra el DataFrame por la fecha proporcionada
    filmaciones = data_total[data_total["release_date"] == fecha_obj]

    return filmaciones.shape[0]


# 3. Funcion Score / Popularidad de la Pelicula  ______________________________________________________________________________________________________________________

def score_titulo(titulo_de_la_filmacion: str):

    # Convertir el título ingresado a minúsculas
    titulo = titulo_de_la_filmacion.lower()

    # Filtrar el DataFrame para encontrar la filmación por título
    titulo = data_total[data_total["title"].str.lower() == titulo]

    if titulo.empty:
        raise HTTPException(status_code=404, detail="Filmación no encontrada")

    # Suponiendo que las columnas son 'titulo', 'año_de_estreno' y 'popularidad'
    resultado = titulo[["title", "release_year", "popularity"]].iloc[0]

    return {
        "Titulo de la Pelicula": resultado["title"],
        "Año de Estreno": resultado["release_year"],
        "Popularidad": resultado["popularity"]
    }


# 4. Funcion Valoraciones de las peliculas ___________________________________________________________________________________________________________________________________

def votos_titulo(titulo_de_la_filmacion: str):
    # Convertir el título ingresado a minúsculas
    titulo_buscado = titulo_de_la_filmacion.lower()

 # Filtrar el DataFrame para encontrar la filmación ignorando mayúsculas
    filmacion = data_total[data_total["title"].str.lower() == titulo_buscado]

    if filmacion.empty:
        raise HTTPException(status_code=404, detail="Filmación no encontrada")

    # Obtener el año de estreno, total de valoraciones y promedio de reseñas
    año_estreno = filmacion["release_year"].iloc[0]
    total_valoraciones = filmacion["vote_count"].sum()
    promedio_reseñas = filmacion["vote_average"].iloc[0]  # Columna de promedio de reseñas // vote_average

    return {
        "Titulo": titulo_de_la_filmacion,
        "Año de estreno": año_estreno,
        "Total de Votos": total_valoraciones,
        "Promedio de Reseñas": promedio_reseñas
    }


# 5. Funcion para Obtener la Informacion de los Actores ____________________________________________________________________________________________________________________________________________

credits = pd.read_parquet("DataSets/df_credits_limpio.parquet")
movies = pd.read_parquet("DataSets/df_movies_limpio.parquet")

# Limpiar la columna de actores
credits["Actores"] = credits["Actores"].str.strip().str.lower()  # Eliminar espacios y convertir a minúsculas

def get_actor(nombre_actor: str):

    # Convertir el nombre del actor a minúsculas para la búsqueda
    nombre_actor = nombre_actor.strip().lower()

    # Filtrar el DataFrame de credits para obtener el actor
    actor_data = credits[credits["Actores"].str.contains(nombre_actor, case=False, na=False)]

    if actor_data.empty:
        return {"error": "Actor no encontrado"}

    # Obtener los IDs de las películas en las que ha participado el actor
    movie_ids = actor_data['id'].unique()

    # Filtrar el DataFrame de movies para obtener las películas del actor
    movies_data = movies[movies['id'].isin(movie_ids)]

    # Calcular la cantidad de películas
    cantidad_peliculas = len(movies_data)

    # Calcular el retorno total
    retorno_total = movies_data["return"].sum()

    # Calcular el promedio de retorno
    promedio = retorno_total / cantidad_peliculas if cantidad_peliculas > 0 else 0.0

    return {
        "nombre de actor": nombre_actor,
        "cantidad de peliculas": cantidad_peliculas,
        "retorno total": retorno_total,
        "promedio de retorno": promedio
    }


# 6. Funcion para Obtener Informacion de los Directores _____________________________________________________________________________________________________________________________________________________________

credits = pd.read_parquet("DataSets/df_credits_limpio.parquet")
movies = pd.read_parquet("DataSets/df_movies_limpio.parquet")

# Limpiar la columna de directores
credits['Diretores'] = credits['Diretores'].str.strip().str.lower()  # Eliminar espacios y convertir a minúsculas

def get_director(nombre_director: str):
    # Convertir el nombre del director a minúsculas para la búsqueda
    nombre_director = nombre_director.strip().lower()

    # Filtrar el DataFrame de credits para obtener el director
    director_data = credits[credits['Diretores'].str.contains(nombre_director, case=False, na=False)]

    if director_data.empty:
        return {"error": "Director no encontrado"}

    # Obtener los IDs de las películas en las que ha trabajado el director
    movie_ids = director_data['id'].unique()

    # Filtrar el DataFrame de movies para obtener las películas del director
    movies_data = movies[movies['id'].isin(movie_ids)]

    # Calcular el retorno total
    retorno_total = movies_data['return'].sum()

    # Crear una lista para almacenar la información de las películas
    peliculas_info = movies_data[['title', 'release_date', 'return', 'budget', 'revenue']].to_dict(orient='records')

    return {
        "Nombre del Director": nombre_director,
        "Retorno total": retorno_total,
        "Peliculas realizadas": peliculas_info
    }


