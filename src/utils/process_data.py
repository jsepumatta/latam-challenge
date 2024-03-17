"""
        Procesa las líneas de un archivo JSON que contiene tweets y devuelve un diccionario que cuenta la actividad
        de usuarios por fecha.

        Argumentos:
        - lines (List[str]): Lista de líneas del archivo JSON que representan tweets.

        Retorna:
        - date_user_dict (dict): Diccionario anidado con contadores que representa la actividad de usuarios por fecha.

        Comentarios:
        - Se inicializa un defaultdict con Counter para almacenar la actividad por fecha y usuario.
        - Para cada línea en las líneas proporcionadas:
            - Se carga el tweet desde la línea en formato JSON utilizando ujson.
            - Se extrae la fecha del tweet y se convierte a un objeto de fecha de Python.
            - Se obtiene el nombre de usuario del tweet.
            - Se actualiza el diccionario anidado incrementando el contador para la fecha y usuario correspondiente.
        - El resultado es un diccionario que muestra la actividad de cada usuario en cada fecha.

        Ejemplo:
        lines = ['{"date": "2022-01-01T12:00:00+00:00", "user": {"username": "user1"}, "text": "Example tweet"}']
        result = process_data(lines)
        # Output: {datetime.date(2022, 1, 1): Counter({'user1': 1})}
        """

import ujson
from typing import List
from datetime import datetime
from collections import defaultdict, Counter


def process_data(lines: List[str]) -> dict:
    """
        Procesa las líneas de un archivo JSON que contiene tweets y devuelve un diccionario que cuenta la actividad
        de usuarios por fecha.

        Argumentos:
        - lines (List[str]): Lista de líneas del archivo JSON que representan tweets.

        Retorna:
        - date_user_dict (dict): Diccionario anidado con contadores que representa la actividad de usuarios por fecha.

        Comentarios:
        - Se inicializa un defaultdict con Counter para almacenar la actividad por fecha y usuario.
        - Para cada línea en las líneas proporcionadas:
            - Se carga el tweet desde la línea en formato JSON utilizando ujson.
            - Se extrae la fecha del tweet y se convierte a un objeto de fecha de Python.
            - Se obtiene el nombre de usuario del tweet.
            - Se actualiza el diccionario anidado incrementando el contador para la fecha y usuario correspondiente.
        - El resultado es un diccionario que muestra la actividad de cada usuario en cada fecha.

        Ejemplo:
        lines = ['{"date": "2022-01-01T12:00:00+00:00", "user": {"username": "user1"}, "text": "Example tweet"}']
        result = process_data(lines)
        # Output: {datetime.date(2022, 1, 1): Counter({'user1': 1})}
        """
    # Se crea un diccionario predeterminado de defaultdict(Counter) para almacenar los usuarios y sus conteos de
    # tweets por fecha.
    date_user_dict = defaultdict(Counter)

    # Se recorre cada línea en 'lines', que contiene datos de tweets en formato JSON.
    for line in lines:
        # Se carga cada tweet en formato JSON utilizando ujson.loads().
        tweet = ujson.loads(line)
        # Se extrae la fecha del tweet y se convierte en un objeto de fecha utilizando datetime.strptime().
        date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00').date()
        # Extraemos el nombre de usuario del tweet.
        user = tweet['user']['username']
        # Se actualiza el diccionario 'date_user_dict' con el conteo de tweets para el usuario en la fecha
        # correspondiente.
        date_user_dict[date][user] += 1

    # Se retorna 'date_user_dict', que contiene las fechas como claves y los nombres de usuario con sus conteos de
    # tweets como valores.
    return date_user_dict
