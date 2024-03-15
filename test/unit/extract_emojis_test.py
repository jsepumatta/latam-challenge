import unittest
from src.utils.extract_emojis import extract_emojis


class TestExtractEmojis(unittest.TestCase):

    def test_extract_emojis(self):
        # Caso de prueba con emojis presentes en el texto
        text_with_emojis = '¡Hola! 😊👍🔥'
        expected_result = ['😊', '👍', '🔥']
        self.assertEqual(extract_emojis(text_with_emojis), expected_result)

        # Caso de prueba con texto sin emojis
        text_without_emojis = 'Este es un texto sin emojis.'
        self.assertEqual(extract_emojis(text_without_emojis), [])

        # Caso de prueba con texto vacío
        empty_text = ''
        self.assertEqual(extract_emojis(empty_text), [])

        # Caso de prueba con texto que contiene solo emojis
        emoji_only_text = '😊👍🔥'
        expected_result_emoji_only = ['😊', '👍', '🔥']
        self.assertEqual(extract_emojis(emoji_only_text), expected_result_emoji_only)


if __name__ == '__main__':
    unittest.main()
