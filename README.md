## 🇪🇸 README.md (Español)

### 📊 **Scraper de Resultados de Búsqueda de Google**

Este script de Python utiliza la API de SerpApi para realizar búsquedas en Google con una lista de palabras clave y extrae los resultados orgánicos, guardándolos en un archivo de Excel. Es una herramienta útil para análisis SEO y marketing digital, permitiendo rastrear la posición de dominios específicos en los resultados de búsqueda para múltiples términos.

-----

### 🚀 **Características**

  - **Búsqueda Automática:** Realiza búsquedas en Google para una lista predefinida de palabras clave.
  - **Extracción de Datos:** Captura el dominio, el título y la posición de los resultados de búsqueda.
  - **Manejo de Datos:** Utiliza `pandas` para estructurar los datos extraídos en un DataFrame.
  - **Exportación a Excel:** Guarda los resultados limpios y organizados en un archivo `.xlsx`.

-----

### ⚙️ **Requisitos**

Asegúrate de tener instaladas las siguientes bibliotecas de Python:

  - `serpapi`
  - `pandas`
  - `openpyxl`

Puedes instalarlas usando `pip3`:

```bash
pip3 install serpapi pandas openpyxl
```

-----

### 🔧 **Configuración y Uso**

1.  **Obtén una Clave de API:** Necesitas una clave de API de **SerpApi**. Si aún no tienes una, regístrate en [serpapi.com](https://serpapi.com/) y obtén tu clave.

2.  **Configura el Código:** Abre el archivo `.py` y reemplaza la cadena vacía en la variable `clave_api` con tu clave:

    ```python
    clave_api = "TU_CLAVE_AQUI"
    ```

3.  **Define tus Palabras Clave:** Modifica la lista `palabras_clave` para incluir los términos que deseas buscar.

4.  **Ejecuta el Script:** Abre una terminal en el directorio del proyecto y ejecuta el script:

    ```bash
    python3 tu_script_nombre.py
    ```

5.  **Revisa los Resultados:** Después de la ejecución, se creará un archivo llamado `resultados_busqueda.xlsx` en el mismo directorio con todos los datos extraídos.

-----

### 🤝 **Contribuciones**

¡Las contribuciones son bienvenidas\! Si tienes ideas para mejorar el script, no dudes en abrir un *issue* o enviar una *pull request*.

-----

## 🇺🇸 README.md (English)

### 📊 **Google Search Results Scraper**

This Python script uses the SerpApi API to perform Google searches for a list of keywords and extracts the organic results, saving them to an Excel file. It's a useful tool for SEO analysis and digital marketing, allowing you to track the position of specific domains in search results for multiple terms.

-----

### 🚀 **Features**

  - **Automated Search:** Performs Google searches for a predefined list of keywords.
  - **Data Extraction:** Captures the domain, title, and position of search results.
  - **Data Handling:** Uses `pandas` to structure the extracted data into a DataFrame.
  - **Excel Export:** Saves the clean and organized results to an `.xlsx` file.

-----

### ⚙️ **Requirements**

Make sure you have the following Python libraries installed:

  - `serpapi`
  - `pandas`
  - `openpyxl`

You can install them using `pip3`:

```bash
pip3 install serpapi pandas openpyxl
```

-----

### 🔧 **Setup and Usage**

1.  **Get an API Key:** You'll need an API key from **SerpApi**. If you don't have one, sign up at [serpapi.com](https://serpapi.com/) and get your key.

2.  **Configure the Code:** Open the `.py` file and replace the empty string in the `clave_api` variable with your key:

    ```python
    api_key = "YOUR_API_KEY_HERE"
    ```

3.  **Define Your Keywords:** Modify the `keywords` list to include the terms you want to search for.

4.  **Run the Script:** Open a terminal in the project directory and run the script:

    ```bash
    python3 your_script_name.py
    ```

5.  **Check the Results:** After execution, a file named `resultados_busqueda.xlsx` will be created in the same directory with all the extracted data.

-----

### 🤝 **Contributions**

Contributions are welcome\! If you have ideas to improve the script, feel free to open an issue or submit a pull request.