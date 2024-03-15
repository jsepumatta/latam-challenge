import unittest
import os
from src.q2_time import q2_time


class TestQ2Time(unittest.TestCase):
    # Se define la ruta al archivo de prueba
    test_file_path = "test_tweets.json"

    def setUp(self):
        # Se crea un archivo de prueba con algunos tweets que contienen emojis
        with open(self.test_file_path, 'w', encoding='utf-8') as f:
            f.write('{"content": "😀🚀🚀"}\n')
            f.write('{"content": "❤️❤️🚀🚀"}\n')
            f.write('{"content": "😀❤️"}\n')
            f.write('{"content": "🚀🚀🚀"}\n')
            f.write('{"content": ""}\n')  # Tweet vacío

    def tearDown(self):
        # Se elimina el archivo de prueba después de ejecutar cada test
        os.remove(self.test_file_path)

    def test_q2_time_result_type(self):
        # Se verifica que el resultado tenga el tipo correcto
        result = q2_time(self.test_file_path)
        self.assertIsInstance(result, list)

    def test_q2_time_result_length(self):
        # Se verifica que el resultado tenga longitud 10
        result = q2_time(self.test_file_path)
        self.assertEqual(len(result), 3)

    def test_q2_time_result_elements(self):
        # Se verifica que cada elemento del resultado sea una tupla
        result = q2_time(self.test_file_path)
        for emoji, count in result:
            self.assertIsInstance(emoji, str)
            self.assertIsInstance(count, int)

    def test_q2_time_result_counts(self):
        # Se verifica que la frecuencia de cada emoji sea un número positivo
        result = q2_time(self.test_file_path)
        for _, count in result:
            self.assertGreaterEqual(count, 0)

    def test_q2_time_file_not_found_error(self):
        # Se verifica que se genere FileNotFoundError si el archivo no existe
        with self.assertRaises(FileNotFoundError):
            q2_time("nonexistent_file.json")


if __name__ == '__main__':
    unittest.main()
