from z3 import *

def goldbach(even: int) -> tuple:
    """Find the two primes that add up to the even number and return them."""
    even_z3 = IntVal(even)
    a, b = Ints("a b")
    fa1, fa2, fb1, fb2 = Ints("fa1 fa2 fb1 fb2")
    s = Solver()
    s.add([
        a > 1,
        b > 1,
        a < even_z3,
        b < even_z3,
        a + b == even_z3,
        Not(Exists([fa1, fa2], And(fa1 < a, fa2 < a, fa1 > 1, fa2 > 1, fa1 * fa2 == a))),
        Not(Exists([fb1, fb2], And(fb1 < b, fb2 < b, fb1 > 1, fb2 > 1, fb1 * fb2 == b)))
    ])
    if(s.check() == sat):
        m = s.model()
        return (m.evaluate(a).as_long(), m.evaluate(b).as_long())
    else:
        return None
