from z3 import *

def prime_number(x):

    a, b = Ints('a b')
    s1 = Solver()
    s1.add(And(x > 1, (x % 1) == 0))

    if(s1.check() == unsat):
        return "not prime"

    s2 = Solver()
    s2.add(a > 1, b > 1, a * b == x)

    if(s2.check() == sat):
        return "not prime"

    return("prime")