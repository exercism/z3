import unittest
from z3 import *
from least_change import (
    least_change,
)

# Tests adapted from https://github.com/exercism/python/blob/main/exercises/practice/change/change_test.py

class ChangeTest(unittest.TestCase):
    def test_single_coin_change(self):
        self.assertEqual(str(least_change([1, 5, 10, 25, 100], 25)), "[10 = 0, 25 = 1, 100 = 0, 5 = 0, min_coins = 1, "
                                                                     "1 = 0]")

    def test_multiple_coin_change(self):
        self.assertEqual(str(least_change([1, 5, 10, 25, 100], 15)), "[10 = 1, 25 = 0, 100 = 0, 5 = 1, min_coins = 2, 1 = 0]")

    def test_change_with_lilliputian_coins(self):
        self.assertEqual(str(least_change([1, 4, 15, 20, 50], 23)), "[15 = 1, 4 = 2, 20 = 0, 50 = 0, min_coins = 3, "
                                                                    "1 = 0]")

    def test_change_with_lower_elbonia_coins(self):
        self.assertEqual(str(least_change([1, 5, 10, 21, 25], 63)), "[5 = 0, 21 = 3, 25 = 0, 10 = 0, min_coins = 3, "
                                                                    "1 = 0]")

    def test_large_target_values(self):
        self.assertEqual(str(least_change([1, 2, 5, 10, 20, 50, 100], 999)).replace('\n', ''), "[5 = 1, 50 = 1, 100 = "
                                                                                               "9, 2 = 2, 20 = 2, "
                                                                                               "10 = 0, min_coins = "
                                                                                               "15, 1 = 0]")

    def test_possible_change_without_unit_coins_available(self):
        self.assertEqual(str(least_change([2, 5, 10, 20, 50], 21)), "[10 = 1, 50 = 0, 2 = 3, 20 = 0, 5 = 1, min_coins "
                                                                    "= 5]")

    def test_another_possible_change_without_unit_coins_available(self):
        self.assertEqual(str(least_change([4, 5], 27)), "[4 = 3, 5 = 3, min_coins = 6]")

    def test_no_coins_make_0_change(self):
        self.assertEqual(least_change([1, 5, 10, 21, 25], 0), None)

    def test_for_change_smaller_than_the_smallest_of_coins(self):
        self.assertEqual(least_change([5, 10], 3), None)

    def test_if_no_combination_can_add_up_to_target(self):
        self.assertEqual(least_change([5, 10], 94), None)

    def test_cannot_find_negative_change_values(self):
        self.assertEqual(least_change([1, 2, 5], -5), None)

if __name__ == "__main__":
    unittest.main()