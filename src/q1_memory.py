"""
Módulo para el procesamiento eficiente de tweets.

Contenido del Módulo: - Funciones: - q1_time(file_path: str) -> List[Tuple[datetime.date, str]]: Utiliza
multiprocesamiento para acelerar el procesamiento de datos en paralelo y obtener las 10 fechas más activas junto con
el usuario más activo en cada una de esas fechas.

    - q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
        Utiliza el paquete ijson para procesar el archivo JSON línea por línea, optimizando la memoria.
        Además, utiliza heapq para encontrar las 10 fechas más activas de manera eficiente.

- Módulos Importados:
    - ijson: Para procesar el archivo JSON línea por línea.
    - typing: Para manejar tipos de datos en las funciones.
    - datetime: Para trabajar con objetos de fecha.
    - collections: Para usar defaultdict y Counter.
    - memory_profiler: Para perfilamiento de memoria.
    - heapq: Para encontrar las N fechas más activas de manera eficiente.

Uso: - Importa el módulo y utiliza las funciones q1_time y q1_memory con la ruta del archivo JSON como argumento. -
Estas funciones devuelven una lista de tuplas que representan las N fechas más activas con el usuario más activo en
cada una.

Ejemplo:
    from module_name import q1_time, q1_memory

    file_path = 'farmers-protest-tweets-2021-2-4.json'
    result_time = q1_time(file_path)
    result_memory = q1_memory(file_path)

    # result_time y result_memory contienen las mismas tuplas de fechas más activas y usuarios más activos.

Nota:
    - Se recomienda ejecutar la función q1_memory si se desea optimizar el uso de memoria durante el procesamiento.
"""

import ujson
from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
import heapq

file = 'farmers-protest-tweets-2021-2-4.json'


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
        Utiliza el paquete ijson para procesar el archivo JSON línea por línea, optimizando la memoria.
        Además, utiliza heapq para encontrar las 10 fechas más activas de manera eficiente.

        Argumentos:
        - file_path (str): Ruta del archivo JSON que contiene los tweets.

        Retorna: - List[Tuple[datetime.date, str]]: Lista de tuplas que representan las 10 fechas más activas con el
        usuario más activo en cada una.

        Comentarios:
        - Utiliza ijson para cargar tweets línea por línea, minimizando el uso de memoria.
        - Se inicializa un defaultdict con Counter para almacenar la actividad por fecha y usuario.
        - Se utiliza la función heapq.nlargest para obtener las 10 fechas más activas de manera eficiente.
        - Se determina el usuario más activo en cada fecha.
        - Devuelve una lista de tuplas con las fechas más activas y los usuarios más activos.

        Ejemplo:
        file_path = 'farmers-protest-tweets-2021-2-4.json'
        result = q1_memory(file_path)
        # Output: [(datetime.date(2021, 2, 1), 'user1'), (datetime.date(2021, 2, 2), 'user2'), ...]
        """
    # Se crea un diccionario predeterminado de defaultdict(Counter) para almacenar los usuarios y sus conteos de
    # tweets por fecha.
    date_user_dict = defaultdict(Counter)

    # Se intenta abrir el archivo especificado en 'file_path' para lectura y procesar cada línea.
    try:
        with open(file_path, 'r') as f:
            for line in f:
                # Se carga cada tweet en formato JSON utilizando ujson.loads().
                tweet = ujson.loads(line)
                # Se extrea la fecha del tweet y la convertimos en un objeto de fecha utilizando datetime.strptime().
                date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00').date()
                # Se extrae el nombre de usuario del tweet.
                user = tweet['user']['username']
                # Se actualiza el diccionario 'date_user_dict' con el conteo de tweets para el usuario en la fecha
                # correspondiente.
                date_user_dict[date][user] += 1
    # Se captura la excepción FileNotFoundError si el archivo no se encuentra.
    except FileNotFoundError:
        raise FileNotFoundError("No se pudo encontrar el archivo: {}".format(file_path))
    # Se captura cualquier otra excepción que ocurra al abrir o procesar el archivo.
    except:
        raise Exception("Error al abrir el archivo: {}".format(file_path))

    # Se verifica si el diccionario 'date_user_dict' está vacío. Si lo está, retornamos una lista vacía.
    if not date_user_dict:
        return []

    # Se utiliza heapq.nlargest para obtener las 10 fechas más activas de manera eficiente.
    top_10_dates = heapq.nlargest(10, date_user_dict.items(), key=lambda x: sum(x[1].values()))

    # Para cada fecha seleccionada, se detrmina el usuario más activo y lo agregamos al resultado.
    result = [(date, max(users.items(), key=lambda x: x[1])[0]) for date, users in top_10_dates]

    # Se retorna el resultado.
    return result
