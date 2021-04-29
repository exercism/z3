import unittest
from z3 import *
from two_product_production_decision import find_production_and_profit

class TwoProductProductionDecision(unittest.TestCase):
    def check(self, a_hours: tuple, b_hours: tuple, total_hours: tuple, prices: tuple, expected_a: int, expected_b: int, expected_profit: int):
        """Checks if the user's program is correct for a test and provides a helpful message if not."""
        qa, qb, profit = find_production_and_profit(a_hours, b_hours, total_hours, prices)
        self.assertEqual(qa, expected_a, f"Error: Quantity of A is wrong (expected {expected_a}, got {qa}.")
        self.assertEqual(qb, expected_b, f"Error: Quantity of B is wrong (expected {expected_b}, got {qb}.")
        self.assertEqual(profit, expected_profit, f"Error: Profit is wrong (expected {expected_profit}, got {profit}.")

    def test_all_normal(self):
        """Tests all cases that produce 3 unique outputs and no errors."""
        cases = [
            [  # All B
                (3, 2, 1.5),
                (2, 1, .5),
                (240, 210, 120),
                (22, 15),
                0, 120, 1800
            ],
            [  # All A
                (5, 4, 3),
                (6, 8, 2),
                (400, 300, 350),
                (40, 25),
                75, 0, 3000
            ],
            [  # Nonzero a and b small numbers
                (1, 2, 1.5),
                (1.5, 1.5, 1),
                (200, 250, 175),
                (14, 12),
                50, 100, 1900
            ],
            [  # Nonzero a and b large numbers
                (6, 8, 9),
                (7, 7, 10),
                (1000, 900, 1200),
                (32, 30),
                39, 84, 3768
            ],
            [  # Too small total hours
                (6, 4, 5),
                (5, 4.5, 5.5),
                (3, 250, 200),
                (25, 22),
                0, 0, 0
            ],
            [  # Limited total hours
                (4, 2, 5),
                (5, 1.5, 6),
                (800, 500, 100),
                (18, 20),
                20, 0, 360
            ],
            [  # Zero price
                (6, 4, 5),
                (5, 4, 6),
                (800, 600, 800),
                (0, 20),
                0, 133, 2660
            ]
        ]
        for case in cases:
            self.check(*case)

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

if __name__ == "__main__":
    unittest.main()
