import unittest
from src.utils.chunk_list import chunk_list


class TestChunkList(unittest.TestCase):
    def test_chunk_list(self):
        # Caso de prueba con una lista vacía
        lst_empty = []
        chunk_size_empty = 3
        self.assertEqual(chunk_list(lst_empty, chunk_size_empty), [])

        # Caso de prueba con una lista de tamaño divisible por el tamaño del fragmento
        lst_divisible = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        chunk_size_divisible = 3
        expected_divisible = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g']]
        self.assertEqual(chunk_list(lst_divisible, chunk_size_divisible), expected_divisible)

        # Caso de prueba con una lista de tamaño no divisible por el tamaño del fragmento
        lst_not_divisible = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        chunk_size_not_divisible = 4
        expected_not_divisible = [['a', 'b', 'c', 'd'], ['e', 'f', 'g']]
        self.assertEqual(chunk_list(lst_not_divisible, chunk_size_not_divisible), expected_not_divisible)


if __name__ == '__main__':
    unittest.main()
