"""
Módulo para dividir una lista en partes de tamaño especificado.

Contenido del Módulo:
- Funciones:
    - chunk_list(lst: List[str], chunk_size: int) -> List[List[str]]:
        Divide una lista en partes de tamaño especificado.

- Módulos Importados:
    - typing: Para manejar tipos de datos en las funciones.

Uso:
    - Importa el módulo y utiliza la función chunk_list con la lista y el tamaño del fragmento como argumentos.
    - La función devuelve una lista de listas, donde cada sublista contiene elementos de la lista original.

Ejemplo:
    from module_name import chunk_list

    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    chunk_size = 3
    result = chunk_list(my_list, chunk_size)
    # Resultado: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g']]
"""
from typing import List


def chunk_list(lst: List[str], chunk_size: int) -> List[List[str]]:
    """
        Divide una lista en partes de tamaño especificado.

        Argumentos:
        - lst (List[str]): Lista a dividir.
        - chunk_size (int): Tamaño de cada fragmento.

        Retorna:
        - List[List[str]]: Lista de listas que representan las partes divididas de la lista original.

        Comentarios:
        - Divide la lista en partes de tamaño especificado.
        - Devuelve una lista de listas, donde cada sublista contiene elementos de la lista original.

        Ejemplo:
        my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        chunk_size = 3
        result = chunk_list(my_list, chunk_size)
        # Resultado: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g']]
        """
    # Divide la lista 'lst' en fragmentos de tamaño 'chunk_size' y devuelve una lista de estos fragmentos.
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
