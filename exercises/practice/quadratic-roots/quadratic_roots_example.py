from z3 import *


def roots(a: float, b: float, c: float) -> tuple:
    """Solves for the two roots of the quadratic expression"""
    x = Real('x')
    r1 = Const("r1", RealSort())
    r2 = Const("r2", RealSort())

    s = Solver()
    s.add(ForAll([x], a * x ** 2 + b * x + c == a * (x - r1) * (x - r2)))
    hasRoots = s.check()
    if(hasRoots == sat):
        return (s.model().eval(r1), s.model().eval(r2))
    else:
        return None
