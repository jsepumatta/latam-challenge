import unittest
import os
from src.q3_time import q3_time


class TestQ3Time(unittest.TestCase):
    def test_q3_time_with_valid_file(self):
        # Crear un archivo de prueba con datos simulados
        test_data = """
        Este es un ejemplo de @usuario1 mencionado.
        @usuario2 también está mencionado varias veces.
        Pero @usuario3 es el más mencionado de todos.
        """
        with open('test_file.json', 'w', encoding='utf-8') as f:
            f.write(test_data)

        # Llamar a la función q3_time con el archivo de prueba
        result = q3_time('test_tweeter.json')

        # Comprobar si la longitud del resultado es igual
        self.assertEqual(len(result), 1)

        # Comprobar si los resultados son correctos
        self.assertEqual(result[0], ('Kisanektamorcha', 2))

        # Eliminar el archivo de prueba después de terminar
        os.remove('test_file.json')

    def test_q3_time_with_not_found_file(self):
        # Llamar a la función q3_time con un archivo inexistente
        # Debería generar una excepción FileNotFoundError
        self.assertEqual(q3_time('non_existent_file.json'), [])


if __name__ == '__main__':
    unittest.main()
