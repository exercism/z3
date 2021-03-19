import unittest
from minima import minima
# from minima_example import minima


def toFloat(x: "ArithRef") -> float:
    """"""
    x = x.as_fraction()
    return float(x.numerator) / float(x.denominator)


class MinimaTest(unittest.TestCase):
    def test_root1(self):
        """Basic difference of squares"""
        self.assertAlmostEqual(toFloat(minima(1, -3, 1, 1)), 1.81640625)




if(__name__ == "__main__"):
    unittest.main()