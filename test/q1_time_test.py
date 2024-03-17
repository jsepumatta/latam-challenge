import unittest
from datetime import date
from src.q1_time import q1_time


class TestQ1TimeIntegration(unittest.TestCase):
    def test_q1_time_integration(self):
        # Define la ruta del archivo JSON para tus pruebas
        file_path = 'test_tweeter.json'

        # Ejecuta la función que estás probando
        result = q1_time(file_path)

        # Comprueba que el resultado tiene el formato esperado
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, tuple) and len(item) == 2 for item in result))

        # Comprueba que el resultado coincide con el esperado
        expect = [(date(2021, 2, 12), 'TV9Bharatvarsh')]
        self.assertEqual(result, expect)

    def test_q1_time_integration_invalid_path(self):
        # Define una ruta de archivo JSON inválida
        invalid_path = 'invalid_path.json'

        # Verifica que la función arroje una excepción al recibir una ruta de archivo JSON inválida
        with self.assertRaises(FileNotFoundError):
            q1_time(invalid_path)

    def test_q1_time_integration_empty_json(self):
        # Define la ruta de un archivo JSON vacío
        empty_json_path = 'empty_tweeter.json'

        # Verifica que la función maneje adecuadamente un archivo JSON vacío
        result = q1_time(empty_json_path)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
