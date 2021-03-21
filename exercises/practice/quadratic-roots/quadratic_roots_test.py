import unittest
from quadratic_roots import roots
import z3


def toFloat(x: z3.RatNumRef) -> float:
    """Converts a Rational Number from z3 to a float that base python can use."""
    x = x.as_fraction()
    return float(x.numerator) / float(x.denominator)


def check(ut, t1: tuple, t2: tuple, places = 7):
    """Checks if two tuples contain the same nearly equivalent elements, regardless of order."""
    if(t1 is None and t2 is None):
        ut.assertTrue(True)
    elif(t2 is None or t2 is None):
        # technically an xor
        ut.assertTrue(False)
    else:
        t1 = tuple(toFloat(x) for x in t1)
        ut.assertTrue((round(t1[0], places) == round(t2[0], places) and round(t1[1], places) == round(t2[1], places)) or
                (round(t1[1], places) == round(t2[0], places) and round(t1[0], places) == round(t2[1], places)))


class QuadraticRootsTest(unittest.TestCase):
    def test_root1(self):
        """Basic difference of squares"""
        check(self, roots(1, 0, -4), (-2, 2))

    def test_root2(self):
        """Same root"""
        check(self, roots(1, 6, 9), (-3, -3))

    def test_root3(self):
        """Imaginary roots"""
        check(self, roots(1, 0, 4), None)

    def test_root4(self):
        """Different roots"""
        check(self, roots(1, 5, 6), (-2, -3))

    def test_root5(self):
        """Leading coefficent"""
        check(self, roots(2, -1, -28), (-3.5, 4))

    def test_root6(self):
        """Two positive roots"""
        check(self, roots(1, -7, 10), (2, 5))


if(__name__ == "__main__"):
    unittest.main()
