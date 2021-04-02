from z3 import *

def missing_number(l: list) -> int:
    """Returns the number that is not in the list."""
    m = Int('m')
    s = Solver()
    equations = [m != IntVal(element) for element in l]
    equations.append(1 <= m)
    equations.append(m <= IntVal(len(l) + 1))
    s.add(equations)
    if(s.check() == sat):
        return s.model().evaluate(m).as_long()
    else:
        return None
