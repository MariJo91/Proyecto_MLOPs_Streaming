from fastapi import FastAPI, HTTPException
from typing import Optional
from funciones import cantidad_filmaciones_mes
from funciones import cantidad_filmaciones_por_fecha_dia
from funciones import score_titulo
from funciones import votos_titulo
from funciones import get_actor
from funciones import get_director



#Creacion de una aplicacion con FastApi

app = FastAPI()

# App de prueba 
@app.get("/")
def presentacion():
    return {
        "Hola": "¡Bienvenido a mi Proyecto de MLOPS en Soy Henry!",
        "Te invito a": "Proyecto con FastAPI - Sistema de Recomendacion.",
        "Autor_proyecto": {
            "DataScientist": "Maria Atencio",
            "Mensaje": "Proyecto Individual N° 1 MLOps "
        },

    }

# ejecutar uvicorn main:app --reload para cargar en el servidors


# ________________________________________________ 1. Funcion Cantidad de Filmaciones por Mes ___________________________________________________________________________________________

@app.get("/cantidad_peliculas_mes/{nombre_mes}")
def get_cantidad_filmaciones_mes(nombre_mes: str):
    cantidad = cantidad_filmaciones_mes(nombre_mes)
    return {"mes": nombre_mes, "cantidad": cantidad}



# _______________________________________________ 2. Funcion Cantidad de Filmaciones por Dia ____________________________________________________________________________________

@app.get("/cantidad_filmaciones_fecha_dia/{fecha}")
def get_cantidad_filmaciones_fecha_dia(fecha: str):
    cantidad = cantidad_filmaciones_por_fecha_dia(fecha)
    return {"fecha": fecha, "cantidad": cantidad}



# _______________________________________________ 3. Funcion para el Score / Popularidad de la Pelicula  ___________________________________________________________________________________________________

@app.get("/score_titulo/{titulo_de_la_filmacion}")
def get_score_titulo(titulo_de_la_filmacion: str):
    return score_titulo(titulo_de_la_filmacion)



# _______________________________________________ 4. Funcion para las Valoraciones por Pelicula _________________________________________________________________________________________________

@app.get("/votos_titulo/{titulo_de_la_filmacion}")
def get_votos_titulo(titulo_de_la_filmacion: str):
    return votos_titulo(titulo_de_la_filmacion)



# _______________________________________________ 5. Funcion para Obtener Informacion de los Actores __________________________________________________________________________________________________

@app.get("/actor/{nombre_actor}")
def actor_endpoint(nombre_actor: str):
    result = get_actor(nombre_actor)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result


# ______________________________________________ 6. Funcion para Obtener Infomacion de los Directores _________________________________________________________________________

@app.get("/director/{nombre_director}")
def director_endpoint(nombre_director: str):
    result = get_director(nombre_director)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result



