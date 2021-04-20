import unittest
from prime_example import prime_number

class PrimeTest(unittest.TestCase):
    def test_prime_number_one(self):
        self.assertEqual(prime_number(0), "not prime")

    def test_prime_number_two(self):
        self.assertEqual(prime_number(1), "not prime")

    def test_prime_number_three(self):
        self.assertEqual(prime_number(2), "prime")

    def test_prime_number_four(self):
        self.assertEqual(prime_number(-2), "not prime")

    def test_prime_number_five(self):
        self.assertEqual(prime_number(2.5), "not prime")

    def test_prime_number_six(self):
        self.assertEqual(prime_number(4), "not prime")

    def test_prime_number_seven(self):
        self.assertEqual(prime_number(-4), "not prime")

    def test_prime_number_eight(self):
        self.assertEqual(prime_number(4.0), "not prime")        

    def test_prime_number_nine(self):
        self.assertEqual(prime_number(5.0), "prime")

    def test_prime_number_ten(self):
        self.assertEqual(prime_number(2520), "not prime")

    def test_prime_number_eleven(self):
         self.assertEqual(prime_number(524287), "prime")

    def test_prime_number_twelve(self):
         self.assertEqual(prime_number(-524287), "not prime")

    def test_prime_number_thirteen(self):
         self.assertEqual(prime_number(524288), "not prime")

    def test_prime_number_fourteen(self):
        self.assertEqual(prime_number(100000000), "not prime")

    def test_prime_number_fifteen(self):
        self.assertEqual(prime_number(-100000000), "not prime")

if __name__ == "__main__":
    unittest.main() 