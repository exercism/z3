import unittest
from z3 import *
from two_product_production_decision import find_production_and_profit

class TwoProductProductionDecision(unittest.TestCase):

    def test_all_b(self):
        a_hours = (3, 2, 1.5)
        b_hours = (2, 1, .5)
        total_hours = (240, 210, 120)
        prices = (22, 15)

        qa, qb, profit = find_production_and_profit(a_hours, b_hours, total_hours, prices)
        self.assertEqual(qa, 0)
        self.assertEqual(qb, 120)
        self.assertEqual(profit, 1800)

    def test_all_a(self):
        a_hours = (5, 4, 3)
        b_hours = (6, 8, 2)
        total_hours = (400, 300, 350)
        prices = (40, 25)

        qa, qb, profit = find_production_and_profit(a_hours, b_hours, total_hours, prices)
        self.assertEqual(qa, 75)
        self.assertEqual(qb, 0)
        self.assertEqual(profit, 3000)

    def test_nonzero_a_and_b_small_numbers(self):
        a_hours = (1, 2, 1.5)
        b_hours = (1.5, 1.5, 1)
        total_hours = (200, 250, 175)
        prices = (14, 12)

        qa, qb, profit = find_production_and_profit(a_hours, b_hours, total_hours, prices)
        self.assertEqual(qa, 50)
        self.assertEqual(qb, 100)
        self.assertEqual(profit, 1900)

    def test_nonzero_a_and_b_large_numbers(self):
        a_hours = (6, 8, 9)
        b_hours = (7, 7, 10)
        total_hours = (1000, 900, 1200)
        prices = (32, 30)

        qa, qb, profit = find_production_and_profit(a_hours, b_hours, total_hours, prices)
        self.assertEqual(qa, 39)
        self.assertEqual(qb, 84)
        self.assertEqual(profit, 3768)

    def test_identical_a_and_b(self):
        a_hours = (5, 6, 5.5)
        b_hours = (5, 6, 5.5)
        total_hours = (500, 650, 600)
        prices = (20, 20)

        qa, qb, profit = find_production_and_profit(a_hours, b_hours, total_hours, prices)

        # Many different optimal combinations of a and b because they are identical
        self.assertEqual(qa + qb, 100)
        self.assertEqual(profit, 2000)

    def test_invalid_hours(self):
        a_hours = (5, 4, 3)
        b_hours = (5, 4.5, 2.5)
        total_hours = (-250, 300, 200)
        prices = (15, 12)

        with self.assertRaises(ArithmeticError):
            qa, qb, profit = find_production_and_profit(a_hours, b_hours, total_hours, prices)

    def test_too_small_total_hours(self):
        a_hours = (6, 4, 5)
        b_hours = (5, 4.5, 5.5)
        total_hours = (3, 250, 200)
        prices = (25, 22)

        qa, qb, profit = find_production_and_profit(a_hours, b_hours, total_hours, prices)
        self.assertEqual(qa, 0)
        self.assertEqual(qb, 0)
        self.assertEqual(profit, 0)

    def test_limited_total_hours(self):
        a_hours = (4, 2, 5)
        b_hours = (5, 1.5, 6)
        total_hours = (800, 500, 100)
        prices = (18 ,20)

        qa, qb, profit = find_production_and_profit(a_hours, b_hours, total_hours, prices)
        self.assertEqual(qa, 20)
        self.assertEqual(qb, 0)
        self.assertEqual(profit, 360)
    
    def test_zero_price(self):
        a_hours = (6, 4, 5)
        b_hours = (5, 4, 6)
        total_hours = (800, 600, 800)
        prices = (0, 20)

        qa, qb, profit = find_production_and_profit(a_hours, b_hours, total_hours, prices)
        self.assertEqual(qa, 0)
        self.assertEqual(qb, 133)
        self.assertEqual(profit, 2660)

if __name__ == "__main__":
    unittest.main() 
