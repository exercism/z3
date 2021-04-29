import unittest
from eight_queens import eight_queens

class EightQueensTester(unittest.TestCase):
    def test(self):
        positions = eight_queens()
        self.assertEqual(len(set(x for (x, y) in positions)), 8, "Error: Not all queens are on a distinct column")
        self.assertEqual(len(set(y for (x, y) in positions)), 8, "Error: Not all queens are on a distinct row")
        self.assertEqual(len(set(x+y for (x, y) in positions)), 8, r"Error: Some queens share a diagonal (\)")
        self.assertEqual(sum(x == y for (x, y) in positions), 1, "Error: Some queens share a diagonal (/)")

if(__name__ == "__main__"):
    unittest.main()
