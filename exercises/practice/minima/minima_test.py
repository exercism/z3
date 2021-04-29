import unittest
from minima import minima
import z3

def toFloat(x: z3.RatNumRef) -> float:
    """"""
    if(isinstance(x, float) or isinstance(x, int)):
        return x
    x = x.as_fraction()
    return float(x.numerator) / float(x.denominator)

def createPoly(a: float, b: float, c: float, d: float) -> "Callable":
    """Returns a function representing a polynomial that can be evaluated for an x."""
    return lambda x: a * x ** 3 + b * x ** 2 + c * x + d

class MinimaTest(unittest.TestCase):
    def checkIsMin(self, f: "Callable", coefs: tuple, x: float) -> None:
        """Checks with unit test asserts that the given x value is a minimum."""
        self.assertLess(f(x), f(x - 0.001), f"Error: value at {x} is not a minimum for polynomial with coefficients {coefs}.")
        self.assertLess(f(x), f(x + 0.001), f"Error: value at {x} is not a minimum for polynomial with coefficients {coefs}.")

    def test_min1(self):
        """Regular cubic function. One local minimum"""
        self.assertAlmostEqual(toFloat(minima(1, -3, 1, 1)), 1.81640625)

    def test_mins(self):
        """Multiple equations. Just check that the values are minima."""
        coeffs = [
            (2, -3, 0, 1),
            (-1, 0, 4, -2),
            (1.6, 0, -0.5, 3)
        ]
        for coef_tup in coeffs:
            f = createPoly(*coef_tup)
            minX = toFloat(minima(*coef_tup))
            self.checkIsMin(f, coef_tup, minX)

if(__name__ == "__main__"):
    unittest.main()
