import unittest
from prime import prime_number

class PrimeTest(unittest.TestCase):
    def check(self, number: int, isPrime: bool):
        """Checks if the user's program correctly determines primality and provides a helpful message if not."""
        self.assertEqual(prime_number(number), isPrime, f"Error: {number} was found {'not ' if isPrime else ''}to be prime.")

    def test_all(self):
        cases = [
            (0, False),
            (1, False),
            (2, True),
            (-2, False),
            (2.5, False),
            (4, False),
            (-4, False),
            (4.0, False),
            (5.0, True),
            (2520, False),
            (524287, True),
            (-524287, False),
            (524288, False),
            (100000000, False),
            (-100000000, False)
        ]
        for case in cases:
            self.check(*case)

if __name__ == "__main__":
    unittest.main()
