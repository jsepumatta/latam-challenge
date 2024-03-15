"""
Encuentra los 10 emojis más utilizados en los tweets.

Esta función lee un archivo JSON que contiene tweets y cuenta la frecuencia de cada emoji presente en el
contenido de los tweets. Luego, devuelve una lista de las 10 tuplas más comunes, donde cada tupla contiene un
emoji y su frecuencia de aparición.

Args:
    file_path (str): La ruta al archivo JSON que contiene los tweets.

Returns:
    List[Tuple[str, int]]: Una lista de las 10 tuplas más comunes, donde cada tupla contiene un emoji (
    representado como una cadena) y su frecuencia de aparición en los tweets.

Raises:
    FileNotFoundError: Si el archivo especificado no existe en la ruta proporcionada.
    Exception: Si ocurre algún error al intentar leer el archivo.

Notas:
    - Los tweets deben estar en formato JSON, donde cada línea representa un tweet.
    - La función utiliza la biblioteca ujson para un procesamiento eficiente del JSON y la biblioteca regex para
    manejar expresiones regulares Unicode.
"""
from typing import List, Tuple
import ujson
import regex as re
from collections import Counter


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Encuentra los 10 emojis más utilizados en los tweets.

    Esta función lee un archivo JSON que contiene tweets y cuenta la frecuencia de cada emoji presente en el
    contenido de los tweets. Luego, devuelve una lista de las 10 tuplas más comunes, donde cada tupla contiene un
    emoji y su frecuencia de aparición.

    Args:
        file_path (str): La ruta al archivo JSON que contiene los tweets.

    Returns:
        List[Tuple[str, int]]: Una lista de las 10 tuplas más comunes, donde cada tupla contiene un emoji (
        representado como una cadena) y su frecuencia de aparición en los tweets.

    Raises:
        FileNotFoundError: Si el archivo especificado no existe en la ruta proporcionada.
        Exception: Sí ocurre algún error al intentar leer el archivo.

    Notas:
        - Los tweets deben estar en formato JSON, donde cada línea representa un tweet.
        - La función utiliza la biblioteca ujson para un procesamiento eficiente del JSON y la biblioteca regex para
        manejar expresiones regulares Unicode.
    """
    emoji_counts = Counter()
    emoji_pattern = re.compile(r'\p{So}')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                tweet = ujson.loads(line)
                content = tweet.get('content', '')
                emojis = emoji_pattern.findall(content)  # Se busca todos los emojis en el contenido del tweet
                emoji_counts.update(
                    emojis)  # Se actualiza el contador de emojis con los emojis encontrados en este tweet
        # Se captura la excepción FileNotFoundError si el archivo no se encuentra.
    except FileNotFoundError:
        raise FileNotFoundError("No se pudo encontrar el archivo: {}".format(file_path))
    # Se captura cualquier otra excepción que ocurra al abrir el archivo.
    except:
        raise Exception("Error al abrir el archivo: {}".format(file_path))

    return emoji_counts.most_common(10)
