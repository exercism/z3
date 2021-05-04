import unittest
from averager import average

class AverageTest(unittest.TestCase):
    def check(self, i1: float, i2: float, exp: float):
        """Checks the inputs for a case with an expected output and prints a helpful message upon failure."""
        average_found = average(i1, i2)
        self.assertEqual(average_found, exp, f"Error: Average of {i1} and {i2} was found to be {average_found}, not {exp}")

    def test_average_one(self):
        self.check(3, 5, 4)

    def test_average_two(self):
        self.check(4, 6, 5)

    def test_average_three(self):
        self.check(100, 200, 150)

    def test_average_four(self):
        self.check(30, 31, 30.5)

    def test_average_five(self):
        self.check(-2, -4, -3)

    def test_average_six(self):
        self.check(-6, 6, 0)
        self.assertEqual(average(-6, 6), 0)

    def test_average_seven(self):
        self.check(0, 6, 3)

    def test_average_eight(self):
        self.check(500, 900, 700)

if __name__ == "__main__":
    unittest.main()
