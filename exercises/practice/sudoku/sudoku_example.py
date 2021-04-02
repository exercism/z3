from z3 import *

def sudoku(puzzle: list) -> list:
    """Solve the sudoku puzzle and return the solution"""
    X = [[Int("x:{},{}".format(row + 1, col + 1)) for col in range(9)] for row in range(9)]

    # each cell contains a value in {1, ..., 9}
    range_constraint = [And(1 <= X[col][row], X[col][row] <= 9) for col in range(9) for row in range(9)]

    # each row contains a digit at most once
    rows_constraint = [Distinct(X[row]) for row in range(9)]

    # each column contains a digit at most once
    columns_constraint = [Distinct([X[row][col] for row in range(9)]) for col in range(9)]

    # each 3x3 square contains a digit at most once
    square_constraint = [Distinct([X[3 * majRow + minRow][3 * majCol + minCol]
                      for minRow in range(3) for minCol in range(3)])
            for majRow in range(3) for majCol in range(3)]

    sudoku_constraints = range_constraint + rows_constraint + columns_constraint + square_constraint

    """
    ((0, 0, 0, 0, 9, 4, 0, 3, 0),
    (0, 0, 0, 5, 1, 0, 0, 0, 7),
    (0, 8, 9, 0, 0, 0, 0, 4, 0),
    (0, 0, 0, 0, 0, 0, 2, 0, 8),
    (0, 6, 0, 2, 0, 1, 0, 5, 0),
    (1, 0, 2, 0, 0, 0, 0, 0, 0),
    (0, 7, 0, 0, 0, 0, 5, 2, 0),
    (9, 0, 0, 0, 6, 5, 0, 0, 0),
    (0, 4, 0, 9, 7, 0, 0, 0, 0))
    """

    # Ensure that the generated sudoku solution works with the fits the given puzzle.
    puzzle_constraint = [If(puzzle[row][col] == 0,
                     True,
                     X[row][col] == puzzle[row][col])
                  for row in range(9) for col in range(9)]

    s = Solver()
    s.add(sudoku_constraints + puzzle_constraint)
    if(s.check() == sat):
        m = s.model()
        r = [[m.evaluate(X[row][col]).as_long() for col in range(9)] for row in range(9)]
        return r
    else:
        return None
