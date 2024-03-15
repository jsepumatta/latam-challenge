"""Módulo para el procesamiento de tweets.

Contenido del Módulo: - Funciones: - q2_memory(file_path: str) -> List[Tuple[str, int]]: Analiza los tweets de un
archivo JSON para contar y devolver los 10 emojis más utilizados. - extract_emojis(text: str) -> List[str]: Extrae
los emojis de un texto dado.

- Módulos Importados:
    - ujson: Para cargar tweets desde el archivo JSON de manera eficiente.
    - typing: Para manejar tipos de datos en las funciones.
    - collections: Para usar el contador de emojis.
    - emoji: Para trabajar con emojis Unicode.
    - memory_profiler: Para perfilamiento de memoria.

Uso: - Importa el módulo y utiliza la función q2_memory con la ruta del archivo JSON como argumento. - La función
devuelve una lista de tuplas que representan los 10 emojis más utilizados y su frecuencia.

Ejemplo:
    from module_name import q2_memory

    file_path = 'farmers-protest-tweets-2021-2-4.json'
    result = q2_memory(file_path)
    # Resultado: [('😊', 120), ('👍', 90), ('🔥', 75), ...]

Nota:
    - Se recomienda ejecutar la función q2_memory si se desea perfilar el uso de memoria durante el procesamiento.
"""

import ujson
from typing import List, Tuple
from collections import Counter
from src.utils.extract_emojis import extract_emojis


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Analiza los tweets de un archivo JSON para contar y devolver los 10 emojis más utilizado.

        Argumentos:
        - file_path (str): Ruta del archivo JSON que contiene los tweets.

        Retorna: - List[Tuple[str, int]]: Lista de tuplas que representan los 10 emojis más utilizados y su
        frecuencia.

        Comentarios: - Utiliza ujson para cargar tweets desde el archivo JSON de manera eficiente. - Utiliza un
        contador de emojis para llevar un seguimiento de la frecuencia de cada emoji. - Extrae los emojis de cada
        tweet utilizando la función extract_emojis. - Devuelve los 10 emojis más utilizados junto con su frecuencia
        en forma de lista de tuplas.

        Ejemplo:
        file_path = 'farmers-protest-tweets-2021-2-4.json'
        result = q2_memory(file_path)
        # Resultado: [('😊', 120), ('👍', 90), ('🔥', 75), ...]
        """

    emoji_counter = Counter()
    try:
        with open(file_path, 'r') as f:
            for line in f:
                tweet = ujson.loads(line)
                emojis = extract_emojis(tweet['content'])
                emoji_counter.update(emojis)
    except FileNotFoundError:
        raise FileNotFoundError("No se pudo encontrar el archivo: {}".format(file_path))
    # Se captura cualquier otra excepción que ocurra al abrir el archivo.
    except:
        raise Exception("Error al abrir el archivo: {}".format(file_path))
    top_10_emojis = emoji_counter.most_common(10)
    return top_10_emojis
