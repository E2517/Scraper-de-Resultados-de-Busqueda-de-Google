import os
import pandas as pd
from urllib.parse import urlparse
from serpapi.google_search import GoogleSearch

# Define la lista de palabras clave y la clave de la API
palabras_clave = [
    "Los Mejores Abogados Penalistas Murcia",
    "Abogado Penalista Murcia",
    "Los 10 Mejores Abogados Penalistas Murcia",
    "Penalista Murcia",
    "Carlos CR Abogogado Penalista"
]

# Lee la clave de API de la variable de entorno
clave_api = os.getenv("SERPAPI_API_KEY")

# Verifica si la clave de la API está configurada
if not clave_api:
    print("La clave de API no está configurada. Por favor, configura el secreto 'SERPAPI_API_KEY' en GitHub.")
    exit()

# Lista para almacenar todos los resultados
todos_los_resultados = []

# Itera sobre cada palabra clave en la lista
for palabra_clave in palabras_clave:
    # Configura los parámetros de la búsqueda
    parametros = {
        "engine": "google",
        "q": palabra_clave,
        "api_key": clave_api,
        "num": 10
    }

    # Realiza la búsqueda
    try:
        busqueda = GoogleSearch(parametros)
        resultados = busqueda.get_dict()

        # Extrae los dominios y los guarda
        if "organic_results" in resultados:
            for resultado in resultados["organic_results"]:
                if "link" in resultado:
                    link = resultado["link"]
                    dominio = urlparse(link).netloc

                    # Crea un diccionario con los datos
                    diccionario_resultado = {
                        "Palabra Clave": palabra_clave,
                        "Dominio": dominio,
                        "Título": resultado.get("title", "No disponible"),
                        "Posición": resultado.get("position", "No disponible")
                    }
                    todos_los_resultados.append(diccionario_resultado)
        else:
            print(f"No se encontraron resultados orgánicos para '{palabra_clave}'.")
    except Exception as e:
        print(f"Error en la búsqueda para '{palabra_clave}': {e}")
        
# Convierte la lista de diccionarios a un DataFrame de pandas
df = pd.DataFrame(todos_los_resultados)

# Guarda el DataFrame en un archivo de Excel
try:
    df.to_excel("resultados_busqueda.xlsx", index=False, engine='openpyxl')
    print("\n✅ Los resultados se han guardado con éxito en 'resultados_busqueda.xlsx'")
except Exception as e:
    print(f"\n❌ Error al guardar el archivo: {e}")
