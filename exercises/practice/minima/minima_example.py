from z3 import *

def minima(a: float, b: float, c: float, d: float):
    """Finds a local minima on the given function."""
    def f(x_):
        return a * x_ ** 3 + b * x_ ** 2 + c * x_ + d

    x = Real("x")
    delta = RealVal(0.001)

    equations = [
        f(x - delta) > f(x),
        f(x + delta) > f(x)
    ]
    s = Solver()
    s.add(equations)
    if(s.check() == sat):
        return s.model().eval(x)
    else:
        return None
