"""
Módulo para procesar datos de tweets y determinar las fechas más activas con el usuario más activo en cada una.

Contenido del Módulo:
    - Funciones:
        - q1_time(file_path: str) -> List[Tuple[datetime.date, str]]: Utiliza multiprocesamiento para procesar datos de
        tweets y encontrar las 10 fechas más activas con el usuario más activo en cada una.

    - Módulos Importados:
        - os: Para obtener el número de núcleos de CPU disponibles.
        - concurrent.futures: Para utilizar la ejecución en paralelo con ProcessPoolExecutor.
        - typing: Para manejar tipos de datos en las funciones.
        - datetime: Para trabajar con objetos de fecha.
        - collections: Para utilizar defaultdict y Counter.
        - src.utils.chunk_list: Módulo personalizado para dividir una lista en partes.
        - src.utils.process_data: Módulo personalizado para procesar los datos de los tweets.

Uso: - Importa el módulo y llama a la función q1_time con la ruta del archivo JSON como argumento. - La función
devuelve una lista de tuplas que representan las 10 fechas más activas y el usuario más activo en cada una.

Ejemplo:
    from module_name import q1_time

    file_path = 'farmers-protest-tweets-2021-2-4.json'
    result = q1_time(file_path)
    # Resultado: [(datetime.date(2021, 2, 1), 'user1'), (datetime.date(2021, 2, 2), 'user2'), ...]
"""

import os
import concurrent.futures
from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
from src.utils.chunk_list import chunk_list
from src.utils.process_data import process_data

file = 'farmers-protest-tweets-2021-2-4.json'


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Procesa datos de tweets y encuentra las 10 fechas más activas con el usuario más activo en cada una.

        Argumentos:
            file_path (str): Ruta del archivo JSON que contiene los tweets.

        Retorna:
            List[Tuple[datetime.date, str]]: Lista de tuplas que representan las 10 fechas más activas y el usuario más
            activo en cada una.

        Excepciones:
            FileNotFoundError: Si no se puede encontrar el archivo especificado.
            Exception: Si ocurre un error al abrir el archivo.

        Comentarios:
            - Utiliza ProcessPoolExecutor para ejecutar procesos en paralelo y acelerar el procesamiento de datos.
            - Divide los datos en partes y procesa cada parte en paralelo.
            - Combina los resultados y encuentra las fechas más activas con el usuario más activo en cada una.

        Ejemplo:
            file_path = 'farmers-protest-tweets-2021-2-4.json'
            result = q1_time(file_path)
            # Resultado: [(datetime.date(2021, 2, 1), 'user1'), (datetime.date(2021, 2, 2), 'user2'), ...]
        """
    # Se intenta abrir el archivo especificado en 'file_path' para lectura.
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    # Se captura la excepción FileNotFoundError si el archivo no se encuentra.
    except FileNotFoundError:
        raise FileNotFoundError("No se pudo encontrar el archivo: {}".format(file_path))
    # Se captura cualquier otra excepción que ocurra al abrir el archivo.
    except:
        raise Exception("Error al abrir el archivo: {}".format(file_path))

    # Se verifica si 'lines' está vacío. Si lo está, se retorna una lista vacía.
    if not lines:
        return []

    # Se determina el número de núcleos de CPU disponibles en el sistema.
    num_cores = os.cpu_count()
    # Se calcula el tamaño de los fragmentos para dividir las líneas en partes para procesamiento paralelo.
    chunk_size = 1 if len(lines) < num_cores else len(lines) // num_cores
    # Se divide la lista de líneas en partes utilizando la función 'chunk_list'.
    parts = chunk_list(lines, chunk_size)

    # Se utiliza un executor de procesos en paralelo para procesar las partes en paralelo.
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Se mapea la función 'process_data' sobre las partes y se obtienen los resultados.
        results = list(executor.map(process_data, parts))

    # Se crea un diccionario predeterminado de defaultdict(Counter) para almacenar los usuarios y sus conteos de
    # tweets por fecha.
    date_user_dict = defaultdict(Counter)
    # Se cambian los resultados de cada proceso en un único diccionario de fecha a usuario y conteo de tweets.
    for result in results:
        for date, user_dict in result.items():
            date_user_dict[date] += user_dict

    # Se ordenan las fechas por la suma total de conteos de tweets en orden descendente y se toman las 10 fechas
    # principales.
    top_10_dates = sorted(date_user_dict.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]
    # Para cada fecha en las 10 principales, se encuentra el usuario con el mayor conteo de tweets y se agrega al
    # resultado.
    result = [(date, max(users.items(), key=lambda x: x[1])[0]) for date, users in top_10_dates]

    # Se retorna el resultado.
    return result
