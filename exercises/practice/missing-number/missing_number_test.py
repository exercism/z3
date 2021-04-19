import unittest
from missing_number import missing_number

class MyTestCase(unittest.TestCase):
    def test50(self):
        """Several tests with numbers in the range of 1 to 50."""
        N = 50
        exclude = [1, 50, 24, 33, 19, 2, 49]
        for ex in exclude:
            found = missing_number(list(range(1, ex)) + list(range(ex + 1, N + 1)))
            self.assertEqual(ex, found)

    def test100(self):
        """Several tests with numbers in the range of 1 to 100."""
        N = 100
        exclude = [1, 100, 50, 24, 33, 19, 2, 49, 10, 80, 70]
        for ex in exclude:
            found = missing_number(list(range(1, ex)) + list(range(ex + 1, N + 1)))
            self.assertEqual(ex, found)

if(__name__ == '__main__'):
    unittest.main()
