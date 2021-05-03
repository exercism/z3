import unittest
from dominoes import possible_chain

# Tests adapted from `problem-specifications//canonical-data.json`

class DominoesTest(unittest.TestCase):

    def test_three_elements(self):
        input_dominoes = [(1, 2), (3, 1), (2, 3)]
        self.assertEqual(possible_chain(input_dominoes), True)

    def test_can_reverse_dominoes(self):
        input_dominoes = [(1, 2), (1, 3), (2, 3)]
        self.assertEqual(possible_chain(input_dominoes), True)

    def test_can_t_be_chained(self):
        input_dominoes = [(1, 2), (4, 1), (2, 3)]
        self.assertEqual(possible_chain(input_dominoes), False)

    def test_disconnected_simple(self):
        input_dominoes = [(1, 1), (2, 2), (3,3)]
        self.assertEqual(possible_chain(input_dominoes), False)

    def test_disconnected_single_isolated(self):
        input_dominoes = [(1, 2), (2, 1), (3, 3)]
        self.assertEqual(possible_chain(input_dominoes), False)

    def test_need_backtrack(self):
        input_dominoes = [(1, 2), (3, 1), (2, 3)]
        self.assertEqual(possible_chain(input_dominoes), True)

if __name__ == "__main__":
    unittest.main()
