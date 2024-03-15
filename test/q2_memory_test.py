import unittest
import ujson
from src.q2_memory import q2_memory


class TestQ2Memory(unittest.TestCase):

    def test_q2_memory(self):
        # Crear un archivo de ejemplo con tweets
        tweets = [
            {"content": "😊👍🔥"},
            {"content": "🚀✨"},
            {"content": "👍💻"}
        ]
        with open('test_tweets.json', 'w') as file:
            for tweet in tweets:
                ujson.dump(tweet, file)
                file.write('\n')

        # Ejecutar la función q2_memory con el archivo de ejemplo
        result = q2_memory('test_tweets.json')

        # Verificar si el resultado es correcto
        expected_result = [('👍', 2),('😊', 1), ('🔥', 1), ('🚀', 1), ('✨', 1), ('💻', 1)]
        self.assertEqual(result, expected_result)

        # Eliminar el archivo de ejemplo después de las pruebas
        import os
        os.remove('test_tweets.json')


if __name__ == '__main__':
    unittest.main()
