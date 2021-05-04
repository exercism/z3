import unittest
from z3 import *
from equilateral_triangle import *

def check(ut, first_point, second_point, expected_third_point_1, expected_third_point_2):
    third_point_1, third_point_2 = generate_third_points(first_point, second_point)

    ut.assertNotEqual(third_point_1, third_point_2, "Error: Both third points are the same.")
    ut.assertTrue(third_point_1 == expected_third_point_1 or third_point_1 == expected_third_point_2,
                  f"No neither point matches {expected_third_point_1}. Have {third_point_1} and {third_point_2}.")
    ut.assertTrue(third_point_2 == expected_third_point_1 or third_point_2 == expected_third_point_2,
                  f"No neither point matches {expected_third_point_2}. Have {third_point_1} and {third_point_2}.")

class EquilateralTriangleTest(unittest.TestCase):
    NUM_DECIMAL_PLACES = 5

    def setUp(self):
        # Display rational numbers as decimals instead of fractions
        set_option(rational_to_decimal=True)

        # Set Precision to 5 decimal places of outputted rational numbers
        set_option(precision=EquilateralTriangleTest.NUM_DECIMAL_PLACES)

    def test_same_y(self):
        first_point = (0, 0)
        second_point = (1, 0)
        expected_third_point_1 = (.5, .86602)
        expected_third_point_2 = (.5, -.86602)
        check(self, first_point, second_point, expected_third_point_1, expected_third_point_2)

    def test_same_x(self):
        first_point = (0, 0)
        second_point = (0, 1)
        expected_third_point_1 = (.86602, .5)
        expected_third_point_2 = (-.86602, .5)
        check(self, first_point, second_point, expected_third_point_1, expected_third_point_2)

    def test_same_point(self):
        first_point = (5.4, 5.4)
        second_point = (5.4, 5.4)
        with self.assertRaises(ArithmeticError):
            third_point_1, third_point_2 = generate_third_points(first_point, second_point)

    def test_arbitrary_points(self):
        test_cases = [
            ((0, 0), (1, 1), (1.36602, -.36602), (-.36602, 1.36602)),
            ((0, 1), (1, 0), (1.36602, 1.36602), (-.36602, -.36602)),
            ((10.6, 4.5), (.6, 11.7), (11.83538, 16.76025), (-.63538, -.56025)),
            ((6.66, 6.66), (9.96, 7.86), (9.34923, 4.40211), (7.27076, 10.11788)),
            ((-5, 4), (-20.6, 3), (-11.93397, -10.00999), (-13.66602, 17.00999)),
            ((-.3, -5.3), (-4.5, -4.1), (-1.36076, -1.06269), (-3.43923, -8.3373)),
            ((15.4, -8.32), (25.2, -17.6), (28.33671, -4.47295), (12.26328, -21.44704))
        ]

        for first_point, second_point, expected_third_point_1, expected_third_point_2 in test_cases:
            check(self, first_point, second_point, expected_third_point_1, expected_third_point_2)

if __name__ == "__main__":
    unittest.main()
