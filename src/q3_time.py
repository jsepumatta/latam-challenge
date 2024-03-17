"""Este módulo proporciona una función para procesar un archivo de texto y encontrar los usuarios más influyentes
basados en menciones.

Funciones: q3_time(file_path: str) -> List[Tuple[str, int]]: Lee un archivo de texto y devuelve una lista de las 10
tuplas más mencionadas de la forma (usuario, cantidad de menciones)."""

import re
from collections import defaultdict
from typing import List, Tuple


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Lee un archivo de texto y devuelve una lista de las 10 tuplas más mencionadas de la forma (usuario, cantidad de
    menciones).

    Args:
        file_path (str): La ruta del archivo de texto a procesar.

    Returns: List[Tuple[str, int]]: Una lista de las 10 tuplas más mencionadas, donde cada tupla contiene el nombre
    de usuario y la cantidad de menciones.
    """
    try:
        user_mentions = defaultdict(int)  # Diccionario para almacenar el recuento de menciones de cada usuario
        mention_pattern = re.compile(r'@(\w+)')  # Expresión regular para buscar menciones de usuario

        with open(file_path, 'r', encoding='utf-8') as file:
            # Se itera sobre cada línea en el archivo
            for line in file:
                mentions = mention_pattern.findall(line)  # Se busca todas las menciones de usuario en la línea
                for mention in mentions:
                    user_mentions[mention] += 1  # Se incrementa el contador de menciones para el usuario

        # Se ordenan los usuarios por cantidad de menciones en orden descendente
        sorted_mentions = sorted(user_mentions.items(), key=lambda x: x[1], reverse=True)
        return sorted_mentions[:10]  # Se devuelven las 10 tuplas más mencionadas

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{file_path}'")
        return []
    except Exception as e:
        print(f"Error al abrir el archivo '{file_path}': {e}")
        return []
