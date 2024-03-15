"""
        Extrae los emojis de un texto dado.

        Argumentos:
        - text (str): Texto del cual extraer los emojis.

        Retorna:
        - List[str]: Lista de emojis extraídos.

        Comentarios:
        - Utiliza la biblioteca emoji para verificar la presencia de emojis en el texto.
        - Devuelve una lista de emojis presentes en el texto.

        Ejemplo:
        text = '¡Hola! 😊👍🔥'
        result = extract_emojis(text)
        # Resultado: ['😊', '👍', '🔥']
        """
import emoji
from typing import List


def extract_emojis(text: str) -> List[str]:
    """
        Extrae los emojis de un texto dado.

        Argumentos:
        - text (str): Texto del cual extraer los emojis.

        Retorna:
        - List[str]: Lista de emojis extraídos.

        Comentarios:
        - Utiliza la biblioteca emoji para verificar la presencia de emojis en el texto.
        - Devuelve una lista de emojis presentes en el texto.

        Ejemplo:
        text = '¡Hola! 😊👍🔥'
        result = extract_emojis(text)
        # Resultado: ['😊', '👍', '🔥']
        """
    return [char for char in text if char in emoji.UNICODE_EMOJI['en']]
