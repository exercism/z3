import unittest
from prime import prime_number

class PrimeTest(unittest.TestCase):
    def test_prime_number_one(self):
        self.assertEqual(prime_number(0), False)

    def test_prime_number_two(self):
        self.assertEqual(prime_number(1), False)

    def test_prime_number_three(self):
        self.assertEqual(prime_number(2), True)

    def test_prime_number_four(self):
        self.assertEqual(prime_number(-2), False)

    def test_prime_number_five(self):
        self.assertEqual(prime_number(2.5), False)

    def test_prime_number_six(self):
        self.assertEqual(prime_number(4), False)

    def test_prime_number_seven(self):
        self.assertEqual(prime_number(-4), False)

    def test_prime_number_eight(self):
        self.assertEqual(prime_number(4.0), False)        

    def test_prime_number_nine(self):
        self.assertEqual(prime_number(5.0), True)

    def test_prime_number_ten(self):
        self.assertEqual(prime_number(2520), False)

    def test_prime_number_eleven(self):
         self.assertEqual(prime_number(524287), True)

    def test_prime_number_twelve(self):
         self.assertEqual(prime_number(-524287), False)

    def test_prime_number_thirteen(self):
         self.assertEqual(prime_number(524288), False)

    def test_prime_number_fourteen(self):
        self.assertEqual(prime_number(100000000), False)

    def test_prime_number_fifteen(self):
        self.assertEqual(prime_number(-100000000), False)

if __name__ == "__main__":
    unittest.main() 