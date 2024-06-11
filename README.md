# Chatbox con Procesamiento de Textos de Recetas

Este proyecto desarrolla un chatbot que puede procesar y dividir la información de un dataset de recetas en ingredientes e instrucciones. Utiliza varias herramientas y bibliotecas de procesamiento de lenguaje natural (NLP) para analizar y dividir el texto.

## Tabla de Contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Instalación](#instalación)
3. [Uso](#uso)
4. [Estructura del Código](#estructura-del-código)
5. [Datasets](#datasets)
6. [Resultados](#resultados)
7. [Licencia](#licencia)

## Descripción del Proyecto

Este proyecto se centra en la creación de un chatbot que puede tomar un dataset de recetas, procesar el texto para dividirlo en ingredientes e instrucciones, y proporcionar respuestas a preguntas sobre las recetas.

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tuusuario/tu-repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd tu-repositorio
    ```
3. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el script principal para iniciar el chatbot:
    ```bash
    python gui.py
    ```
2. Una vez que la GUI esté abierta, puedes cargar los documentos PDF y hacer preguntas sobre las recetas.

## Estructura del Código

- `gui.py`: Contiene el código para la interfaz gráfica de usuario.
- `text_processing.py`: Contiene las funciones para cargar, procesar y dividir los textos de las recetas.
- `requirements.txt`: Lista de dependencias necesarias para el proyecto.
- `images/`: Carpeta que contiene las imágenes utilizadas en la GUI.
- `source_documents/`: Carpeta donde se almacenan los PDF de recetas.

## Datasets

Utilizamos los siguientes datasets para este proyecto:
- [Nutrition details for most common foods](https://www.kaggle.com/datasets/niharika41298/nutrition-details-for-most-common-foods)
- [Food ingredients and recipe dataset with images](https://www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images)

## Resultados

- **Distribución de Recetas:** El dataset contiene varias categorías como desayunos, almuerzos y cenas.
- **Frecuencia de Ingredientes:** Los ingredientes más comunes incluyen X, Y y Z.
- **Evaluación de la Precisión:** Utilizamos métricas como la exactitud y la precisión para evaluar el rendimiento del modelo.
- **Análisis de Errores:** El modelo tuvo éxito en la mayoría de los casos, pero falló en casos donde las instrucciones estaban mal estructuradas o incompletas.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
