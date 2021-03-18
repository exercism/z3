import unittest
from z3 import *
from example import *

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

        third_point_1, third_point_2 = generate_third_points(first_point, second_point)

        self.assertNotEqual(third_point_1, third_point_2)
        self.assertTrue(third_point_1 == expected_third_point_1 or third_point_1 == expected_third_point_2)
        self.assertTrue(third_point_2 == expected_third_point_1 or third_point_2 == expected_third_point_2)

    def test_same_x(self):
        first_point = (0, 0)
        second_point = (0, 1)
        expected_third_point_1 = (.86602, .5)
        expected_third_point_2 = (-.86602, .5)

        third_point_1, third_point_2 = generate_third_points(first_point, second_point)

        self.assertNotEqual(third_point_1, third_point_2)
        self.assertTrue(third_point_1 == expected_third_point_1 or third_point_1 == expected_third_point_2)
        self.assertTrue(third_point_2 == expected_third_point_1 or third_point_2 == expected_third_point_2)

    def test_same_point(self):
        first_point = (5.4, 5.4)
        second_point = (5.4, 5.4)

        with self.assertRaises(ArithmeticError):
            third_point_1, third_point_2 = generate_third_points(first_point, second_point)

    def test_45_degrees(self):
        first_point = (0, 0)
        second_point = (1, 1)
        expected_third_point_1 = (1.36602, -.36602)
        expected_third_point_2 = (-.36602, 1.36602)

        third_point_1, third_point_2 = generate_third_points(first_point, second_point)

        self.assertNotEqual(third_point_1, third_point_2)
        self.assertTrue(third_point_1 == expected_third_point_1 or third_point_1 == expected_third_point_2)
        self.assertTrue(third_point_2 == expected_third_point_1 or third_point_2 == expected_third_point_2)

    def test_negative_45_degrees(self):
        first_point = (0, 1)
        second_point = (1, 0)
        expected_third_point_1 = (1.36602, 1.36602)
        expected_third_point_2 = (-.36602, -.36602)

        third_point_1, third_point_2 = generate_third_points(first_point, second_point)

        self.assertNotEqual(third_point_1, third_point_2)
        self.assertTrue(third_point_1 == expected_third_point_1 or third_point_1 == expected_third_point_2)
        self.assertTrue(third_point_2 == expected_third_point_1 or third_point_2 == expected_third_point_2)

    def test_first_quadrant_1(self):
        first_point = (10.6, 4.5)
        second_point = (.6, 11.7)
        expected_third_point_1 = (11.83538, 16.76025)
        expected_third_point_2 = (-.63538, -.56025)

        third_point_1, third_point_2 = generate_third_points(first_point, second_point)

        self.assertNotEqual(third_point_1, third_point_2)
        self.assertTrue(third_point_1 == expected_third_point_1 or third_point_1 == expected_third_point_2)
        self.assertTrue(third_point_2 == expected_third_point_1 or third_point_2 == expected_third_point_2)

    def test_first_quadrant_2(self):
        first_point = (6.66, 6.66)
        second_point = (9.96, 7.86)
        expected_third_point_1 = (9.34923, 4.40211)
        expected_third_point_2 = (7.27076, 10.11788)

        third_point_1, third_point_2 = generate_third_points(first_point, second_point)

        self.assertNotEqual(third_point_1, third_point_2)
        self.assertTrue(third_point_1 == expected_third_point_1 or third_point_1 == expected_third_point_2)
        self.assertTrue(third_point_2 == expected_third_point_1 or third_point_2 == expected_third_point_2)

    def test_second_quadrant_1(self):
        first_point = (-5, 4)
        second_point = (-20.6, 3)
        expected_third_point_1 = (-11.93397, -10.00999)
        expected_third_point_2 = (-13.66602, 17.00999)

        third_point_1, third_point_2 = generate_third_points(first_point, second_point)

        self.assertNotEqual(third_point_1, third_point_2)
        self.assertTrue(third_point_1 == expected_third_point_1 or third_point_1 == expected_third_point_2)
        self.assertTrue(third_point_2 == expected_third_point_1 or third_point_2 == expected_third_point_2)

    def test_third_quadrant_1(self):
        first_point = (-.3, -5.3)
        second_point = (-4.5, -4.1)
        expected_third_point_1 = (-1.36076, -1.06269)
        expected_third_point_2 = (-3.43923, -8.3373)

        third_point_1, third_point_2 = generate_third_points(first_point, second_point)

        self.assertNotEqual(third_point_1, third_point_2)
        self.assertTrue(third_point_1 == expected_third_point_1 or third_point_1 == expected_third_point_2)
        self.assertTrue(third_point_2 == expected_third_point_1 or third_point_2 == expected_third_point_2)

    def test_fourth_quadrant_1(self):
        first_point = (15.4, -8.32)
        second_point = (25.2, -17.6)
        expected_third_point_1 = (28.33671, -4.47295)
        expected_third_point_2 = (12.26328, -21.44704)

        third_point_1, third_point_2 = generate_third_points(first_point, second_point)

        self.assertNotEqual(third_point_1, third_point_2)
        self.assertTrue(third_point_1 == expected_third_point_1 or third_point_1 == expected_third_point_2)
        self.assertTrue(third_point_2 == expected_third_point_1 or third_point_2 == expected_third_point_2)

if __name__ == "__main__":
    unittest.main()