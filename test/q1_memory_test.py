import unittest
from datetime import date
from src.q1_memory import q1_memory


class TestQ1Memory(unittest.TestCase):
    def test_q1_memory_integration(self):
        # Define la ruta del archivo JSON para tus pruebas
        file_path = 'test_tweeter.json'

        # Ejecuta la función que estás probando
        result = q1_memory(file_path)

        # Comprueba que el resultado tiene el formato esperado
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, tuple) and len(item) == 2 for item in result))
        self.assertTrue(all(isinstance(item[0], date) and isinstance(item[1], str) for item in result))

        # Comprueba que la longitud del resultado sea al menos 10
        self.assertGreaterEqual(len(result), 1)

    def test_q1_time_integration_invalid_path(self):
        # Define una ruta de archivo JSON inválida
        invalid_path = 'invalid_path.json'

        # Verifica que la función arroje una excepción al recibir una ruta de archivo JSON inválida
        with self.assertRaises(FileNotFoundError):
            q1_memory(invalid_path)

    def test_q1_time_integration_empty_json(self):
        # Define la ruta de un archivo JSON vacío
        empty_json_path = 'empty_tweeter.json'

        # Verifica que la función maneje adecuadamente un archivo JSON vacío
        result = q1_memory(empty_json_path)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()