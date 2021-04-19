from z3 import *

def eight_queens() -> list:
    """Find positions for 8 queens such that no two can attack each other."""
    queens = [Int("Q{}".format(i + 1)) for i in range(8)]

    val_c = [And(1 <= queens[i], queens[i] <= 8) for i in range(8)]
    col_c = [Distinct(queens)]
    diag_c = [If(i == j, True, And(queens[i] - queens[j] != i - j, queens[i] - queens[j] != j - i)) for i in range(8) for j in range(i)]
    s = Solver()
    s.add(val_c + col_c + diag_c)
    if(s.check() == sat):
        m = s.model()
        return [(i, m.evaluate(el).as_long()) for (i, el) in enumerate(queens)]
    else:
        return None
