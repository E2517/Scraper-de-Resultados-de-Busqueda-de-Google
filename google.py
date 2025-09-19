from serpapi import GoogleSearch

# Define la lista de palabras clave y la clave de la API
palabras_clave = [
    "Los Mejores Abogados Penalistas Murcia",
    "Abogado Penalista Murcia",
    "Los 10 Mejores Abogados Penalistas Murcia",
    "Penalista Murcia",
    "Carlos CR Abogogado Penalista"
]
clave_api = ""  # Reemplaza con tu clave de API

# Itera sobre cada palabra clave en la lista
for palabra_clave in palabras_clave:
    # Configura los parámetros de la búsqueda para la palabra clave actual
    parametros = {
        "engine": "google",
        "q": palabra_clave,
        "api_key": clave_api,
        "num": 10
    }

    # Realiza la búsqueda
    busqueda = GoogleSearch(parametros)
    resultados = busqueda.get_dict()

    # Extrae y muestra los dominios para la palabra clave actual
    if "organic_results" in resultados:
        print(f"\n--- Resultados para la palabra clave: '{palabra_clave}' ---")
        for resultado in resultados["organic_results"]:
            if "link" in resultado:
                link = resultado["link"]
                # Extrae solo el dominio del enlace
                from urllib.parse import urlparse
                dominio = urlparse(link).netloc
                print(dominio)
    else:
        print(f"No se encontraron resultados orgánicos para '{palabra_clave}'.")
