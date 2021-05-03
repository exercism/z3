from z3 import *
import itertools

def possible_chain(dominoes):

    # Unroll tuples into a flat list
    domino_values = list(itertools.chain(*dominoes))

    # Declare Z3 integers
    a,b,c,d,e,f = Ints('a b c d e f')
   
    # Possible solutions for three dominoes
    equations = [Or(And(a == c, b == f, d == e),
        And(a == c, b == e, d == f),
        And(a == d, b == f, c == e),
        And(a == d, b == e, c == f),
        And(a == e, b == c, d == f),
        And(a == e, b == d, c == f),
        And(a == f, b == c, d == e),
        And(a == f, b == d, c == e)
    )]

    # Map given dominoes to constraints
    constraints = [And(a == IntVal(domino_values[0]),
        b == IntVal(domino_values[1]),
        c == IntVal(domino_values[2]),
        d == IntVal(domino_values[3]),
        e == IntVal(domino_values[4]),
        f == IntVal(domino_values[5]))]
        
    # Run Z3
    s = Solver()
    s.add(constraints)
    s.add(equations)

    # Return result
    is_sat = s.check()
    if is_sat == sat:
        return True
    return False
