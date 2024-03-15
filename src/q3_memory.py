"""
Módulo para analizar un archivo de texto y encontrar los usuarios más influyentes basados en menciones.

Funciones:
    q3_memory(file_path: str) -> List[Tuple[str, int]]: Lee un archivo de texto y devuelve una lista de las 10 tuplas
    más mencionadas de la forma (usuario, cantidad de menciones).
"""
from typing import List, Tuple
from collections import defaultdict


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
       Lee un archivo de texto y devuelve una lista de las 10 tuplas más mencionadas de la forma (usuario, cantidad de
       menciones).

       Args:
           file_path (str): La ruta del archivo de texto a procesar.

       Returns: List[Tuple[str, int]]: Una lista de las 10 tuplas más mencionadas, donde cada tupla contiene el
       nombre de usuario y la cantidad de menciones.
    """
    unique_users = set()  # Conjunto para almacenar usuarios únicos con menciones
    user_mentions = defaultdict(int)  # Diccionario para almacenar recuentos de menciones de usuario

    # Extraccion de usuarios únicos y contar menciones por usuario
    try:
        # Intentar abrir el archivo
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if '@' in line:
                    words = line.split()
                    for word in words:
                        if word.startswith('@'):
                            user = word[1:]
                            unique_users.add(user)  # Agregar usuario único al conjunto
                            user_mentions[user] += 1  # Incrementar el contador de menciones para el usuario
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")
        return []

    # Ordenar los usuarios por cantidad de menciones en orden descendente
    sorted_mentions = sorted(user_mentions.items(), key=lambda x: x[1], reverse=True)
    return sorted_mentions[:10]  # Devolver las 10 tuplas más mencionadas
