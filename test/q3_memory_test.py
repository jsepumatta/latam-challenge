import unittest
import tempfile
import os
from src.q3_memory import q3_memory


class TestQ3Memory(unittest.TestCase):
    def setUp(self):
        # Crear un archivo de prueba con contenido conocido
        self.test_file_content = """Este es un tweet de ejemplo @usuario1
                                    Otro tweet @usuario2 y @usuario1
                                    Último tweet @usuario3"""
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8')
        self.test_file.write(self.test_file_content)
        self.test_file.close()

    def tearDown(self):
        # Eliminar el archivo de prueba después de las pruebas
        os.unlink(self.test_file.name)

    def test_q3_memory(self):
        # Ejecutar la función q3_memory con el archivo de prueba
        result = q3_memory(self.test_file.name)

        # Verificar el resultado esperado
        expected_result = [('usuario1', 2), ('usuario2', 1), ('usuario3', 1)]
        self.assertEqual(result, expected_result, "El resultado no coincide con el esperado")

    def test_file_not_found_error(self):
        # Prueba el manejo de FileNotFoundError
        non_existing_file = "non_existing_file.txt"
        result = q3_memory(non_existing_file)
        self.assertEqual(result, [], "La función no devuelve una lista vacía para FileNotFoundError")

    def test_other_errors(self):
        # Prueba el manejo de otros errores al abrir el archivo
        # Puedes simular un error pasando un directorio en lugar de un archivo
        invalid_path = "/invalid/path/to/file.txt"
        result = q3_memory(invalid_path)
        self.assertEqual(result, [], "La función no devuelve una lista vacía para otros errores al abrir el archivo")


if __name__ == '__main__':
    unittest.main()
