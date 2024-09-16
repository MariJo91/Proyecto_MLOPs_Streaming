

#         Proyecto de Machine Learning Operations (MLOps): Sistema de Recomendacion de Peliculas para Usuarios

### Proyecto

En este proyecto se exploró el rol del MLOps Engineer, combinando habilidades de ingeniería de datos y ciencia de datos para construir un pipeline de Machine Learning completo. A través de la colaboración con la comunidad de datos y el uso de conjuntos de datos públicos, se desarrolló un producto mínimo viable que demuestra cómo los modelos de Machine Learning pueden ser utilizados para mejorar la experiencia del usuario en plataformas Streaming. Este proyecto es un primer paso en un camino continuo de aprendizaje y desarrollo.

### Objetivos del Proyecto

- Construir un sistema de recomendación de Peliculas inteligente utilizando técnicas de Machine Learning para plataformas Streaming.
- Se buscó desarrollar una solución que pudiera ser fácilmente replicada en otros proyectos, demostrando la viabilidad de utilizar estas tecnicas.
- Adquirir experiencia práctica en MLOps y aplicar estas habilidades a un caso de uso real.


![Gráfico de Etapas MLOps](https://github.com/user-attachments/assets/51e07376-726f-41e2-b7e3-fbb389ea36fb)

## - 1. Proceso EDA (Análisis Exploratorio de Datos)

El Proceso EDA fue esencial para comprender la naturaleza de los datos y establecer una línea base para el proyecto. Los resultados obtenidos en esta etapa guiaron las decisiones de diseño de la arquitectura del sistema y la selección de los algoritmos de machine learning más adecuados. Al identificar las características más relevantes de los datos y las relaciones entre ellas, se pudo optimizar el rendimiento del modelo y garantizar la calidad de las predicciones.

El EDA se llevó a cabo utilizando Pandas para la manipulación de datos y Matplotlib y Seaborn para la visualización. Se calcularon estadísticas descriptivas como la media, mediana y desviación estándar para cada variable numérica. Además, se crearon histogramas, diagramas de caja y matrices de correlación para analizar la distribución de los datos y las relaciones entre las variables. Se identificaron outliers utilizando el método de los cuartiles y se imputaron los valores faltantes mediante la media.

## - 2. Proceso ETL (Extracción, Transformación y Carga)

-. Extracción (Extract)
Cargar Datos: El primer paso consistió en extraer los datos de una fuente inicial, Adjunto Archivo Drive: https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5 , una base de datos o cualquier otra fuente de datos estructurada.
Ejemplo: Utilizamos pandas para leer un archivo CSV que contenía información sobre películas, incluyendo columnas como budget, revenue, rating, etc.

-. Transformación (Transform)
Limpieza de Datos: En esta etapa, se realizaron diversas operaciones para limpiar y preparar los datos:

Eliminación de Valores Nulos: Se revisaron las columnas para identificar y manejar valores nulos.
Conversión de Tipos de Datos: Se aseguraron de que las columnas tuvieran los tipos de datos correctos (por ejemplo, convertir la columna de fechas a un tipo de fecha).
Normalización de Nombres de Columnas: Se estandarizó el formato de los nombres de las columnas para facilitar su uso posterior.
Transformaciones Adicionales: Se realizaron otras transformaciones según las necesidades del análisis, como la creación de nuevas columnas, la agrupación de datos, o la aplicación de funciones estadísticas.

-. Carga (Load)
Carga a la API: Finalmente, los datos transformados se prepararon para ser enviados a una API:

Formato de Datos: Se aseguró que los datos estuvieran en un formato adecuado (En este caso Parquet) para la carga a la API.

Este flujo de trabajo permite asegurar la calidad y la utilidad de los datos en cualquier análisis o aplicación futura.

## - 3. Sistema de Recomendacion

Modelo de Recomendación: Con el objetivo de proporcionar recomendaciones precisas y eficientes a medida que crece la base de datos de peliculas, se optó por un enfoque basado en similitud de ítems. Utilizando la técnica de CountVectorizer para representar las filmaciones como vectores numéricos y la métrica de similitud del coseno para comparar estos vectores, se logró desarrollar un modelo escalable y capaz de generar recomendaciones en tiempo real.

## - 4. Implementación de MLOps

Con el objetivo de poner el modelo de recomendación a disposición de los usuarios, se desplegó como una API en la plataforma Render. Esta elección permite una fácil implementación y escalabilidad del servicio. Para automatizar el proceso de despliegue, se configuró una integración continua con GitHub, lo que garantiza que los cambios en el código se reflejen rápidamente en la API. Enlace a la Api https://proyecto-mlops-streaming.onrender.com/docs

## - 5. Video Explicativo

 Se creó un tutorial en video para guiar a los usuarios en el uso de la API. En este video se muestra cómo realizar consultas a la API y se explican los resultados obtenidos, proporcionando una introducción clara y concisa a las capacidades del modelo de recomendación. Link al video:

## - 6. Estructura del Repositorio
  
- Notebooks: Contiene los cuadernos de Jupyter / formato ipynb que documentan el proceso de ETL (Extracción, Transformación y Carga) y el análisis exploratorio de datos.
- images: Almacena los recursos visuales y complementarios utilizados en el proyecto.
- Dataset: Contiene Los datos después de aplicar las transformaciones necesarias.

### Mejoras para un Futuro Proyecto

Este proyecto abarca tres áreas clave: el proceso ETL, el Análisis Exploratorio de Datos (EDA) y el sistema de recomendación de películas.

Para el Proceso ETL:

Automatización: Implementar un flujo de trabajo automatizado para la ejecución periódica del proceso.
Manejo de Errores: Mejorar el logging y la gestión de errores para facilitar la resolución de problemas.

Para el EDA:

Visualizaciones Interactivas: Incorporar herramientas de visualización de datos interactivas para facilitar la interpretación de los resultados.
Validaciones de Datos: Ampliar las validaciones para asegurar la calidad de los datos analizados.

Para el Sistema de Recomendación:

Mejorar Algoritmos: Explorar diferentes algoritmos de recomendación (como filtrado colaborativo y basado en contenido) para optimizar la precisión de las sugerencias.
Personalización: Implementar opciones de personalización que permitan a los usuarios ajustar sus preferencias de recomendación.

Conclusión
La implementación de estas mejoras en las tres áreas del proyecto no solo optimizará el rendimiento y la calidad de los resultados, sino que también enriquecerá la experiencia del usuario, haciendo el sistema más robusto y adaptable a futuras necesidades.




