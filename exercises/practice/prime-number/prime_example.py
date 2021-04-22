from z3 import *

def prime_number(x):

    a, b = Ints('a b')
    s = Solver()

    s.push()
    s.add(And(x > 1, (x % 1) == 0))
    if(s.check() == unsat):
        return False
    s.pop()

    s.add(a > 1, b > 1, a * b == x)
    if(s.check() == sat):
        return False

    return(True)