import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def SetUp(self):
        self.input = [['a', 'b', 'c', 'd'],
                      ['a', 'b', 'c', 'd'],
                      ['a', 'b', 'c', 'd']]

    def test_get_input(self):
        self.input1 = [['a', 'c', 'd'],
                       ['a', 'a', 'e'],
                       ['a', '', 'f']]
        self.input2 = [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['a'], ['g'], ['h'], ['i']]

        self.assertEqual(find_paths_for_elements_in_last_column(self.input1, 3),
                         {'a': [1, 3, 4], 'b': [0, 0, 0], 'c': [1, 0, 0], 'd': [1, 0, 0], 'e': [0, 1, 0],
                          'f': [0, 0, 1], 'g': [0, 0, 0], 'h': [0, 0, 0], 'i': [0, 0, 0], 'j': [0, 0, 0],
                          'k': [0, 0, 0], 'l': [0, 0, 0], 'm': [0, 0, 0], 'n': [0, 0, 0], 'o': [0, 0, 0],
                          'p': [0, 0, 0], 'q': [0, 0, 0], 'r': [0, 0, 0], 's': [0, 0, 0], 't': [0, 0, 0],
                          'u': [0, 0, 0], 'v': [0, 0, 0], 'w': [0, 0, 0], 'x': [0, 0, 0], 'y': [0, 0, 0],
                          'z': [0, 0, 0]})
        self.assertEqual(find_paths_for_elements_in_last_column(self.input2, 10),
                         {'a': [1, 0, 0, 0, 0, 0, 2, 0, 0, 0], 'b': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                          'c': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 'd': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                          'e': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 'f': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                          'g': [0, 0, 0, 0, 0, 0, 0, 2, 0, 0], 'h': [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
                          'i': [0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 'j': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          'k': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'l': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          'm': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'n': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          'o': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'p': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          'q': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'r': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          's': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 't': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          'u': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'v': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          'w': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'x': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          'y': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'z': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})

        self.input3 = [['a', 'a', 'a', 'a', 'a', 'a'],
                       ['a', 'a', 'a', 'a', 'a', 'a'],
                       ['a', 'a', 'a', 'a', 'a', 'a'],
                       ['a', 'a', 'a', 'a', 'a', 'a'],
                       ['a', 'a', 'a', 'a', 'a', 'a'],
                       ['a', 'a', 'a', 'a', 'a', 'a'],
                       ['a', '', '', '', '', 'a']]

        self.assertEqual(find_paths_for_elements_in_last_column(self.input3, 7),
        {'a': [6, 36, 252, 1764, 12348, 86436, 201684], 'b': [0, 0, 0, 0, 0, 0, 0], 'c': [0, 0, 0, 0, 0, 0, 0],
         'd': [0, 0, 0, 0, 0, 0, 0], 'e': [0, 0, 0, 0, 0, 0, 0], 'f': [0, 0, 0, 0, 0, 0, 0], 'g': [0, 0, 0, 0, 0, 0, 0],
         'h': [0, 0, 0, 0, 0, 0, 0], 'i': [0, 0, 0, 0, 0, 0, 0], 'j': [0, 0, 0, 0, 0, 0, 0], 'k': [0, 0, 0, 0, 0, 0, 0],
         'l': [0, 0, 0, 0, 0, 0, 0], 'm': [0, 0, 0, 0, 0, 0, 0], 'n': [0, 0, 0, 0, 0, 0, 0], 'o': [0, 0, 0, 0, 0, 0, 0],
         'p': [0, 0, 0, 0, 0, 0, 0], 'q': [0, 0, 0, 0, 0, 0, 0], 'r': [0, 0, 0, 0, 0, 0, 0], 's': [0, 0, 0, 0, 0, 0, 0],
         't': [0, 0, 0, 0, 0, 0, 0], 'u': [0, 0, 0, 0, 0, 0, 0], 'v': [0, 0, 0, 0, 0, 0, 0], 'w': [0, 0, 0, 0, 0, 0, 0],
         'x': [0, 0, 0, 0, 0, 0, 0], 'y': [0, 0, 0, 0, 0, 0, 0], 'z': [0, 0, 0, 0, 0, 0, 0]})


if __name__ == '__main__':
    unittest.main()