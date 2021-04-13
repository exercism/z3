import unittest
from averager import average

class AverageTest(unittest.TestCase):
    def test_average_one(self):
        self.assertEqual(average(3, 5), 4)

    def test_average_two(self):
        self.assertEqual(average(4, 6), 5)

    def test_average_three(self):
        self.assertEqual(average(100, 200), 150)

    def test_average_four(self):
        self.assertEqual(average(30, 31), 30.5)

    def test_average_five(self):
        self.assertEqual(average(-2, -4), -3)

    def test_average_six(self):
        self.assertEqual(average(-6, 6), 0)

    def test_average_seven(self):
        self.assertEqual(average(0, 6), 3)

    def test_average_eight(self):
        self.assertEqual(average(500, 900), 700)

if __name__ == "__main__":
    unittest.main() 