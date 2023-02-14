import unittest
from sudoku import sudoku

class SudokuTest(unittest.TestCase):
    def checkIsValid(self, problem: list, solution: list) -> None:
        """Checks that a given solution is valid for its problem setup"""
        validNumbers = set(range(1, 9 + 1))
        # Check that all the numbers used
        self.assertTrue(all(set(row) == validNumbers for row in solution))
        self.assertTrue(all(set(row[col] for col in range(9)) == validNumbers for row in solution))
        self.assertTrue(all(
            set(solution[majRow + minRow][majCol + mincol] for minRow in range(3) for mincol in range(3)) == validNumbers
                            for majRow in range(0, 9, 3) for majCol in range(0, 9, 3)
        ))
        self.assertTrue(all(
            (numP == 0 or numP == numS for (numP, numS) in zip(rowP, rowS))
                            for (rowP, rowS) in zip(problem, solution)
        ))

    def test1(self):
        problem = [(0, 0, 0, 0, 9, 4, 0, 3, 0),
            (0, 0, 0, 5, 1, 0, 0, 0, 7),
            (0, 8, 9, 0, 0, 0, 0, 4, 0),
            (0, 0, 0, 0, 0, 0, 2, 0, 8),
            (0, 6, 0, 2, 0, 1, 0, 5, 0),
            (1, 0, 2, 0, 0, 0, 0, 0, 0),
            (0, 7, 0, 0, 0, 0, 5, 2, 0),
            (9, 0, 0, 0, 6, 5, 0, 0, 0),
            (0, 4, 0, 9, 7, 0, 0, 0, 0)]
        solution = sudoku(problem)
        self.checkIsValid(problem, solution)
        
    def testall(self):
        with open("sudoku_problems.txt", 'r') as problems_file:
            # Problems copied from Project Euler, problem 96
            num_tests = 10
            for i in range(num_tests):
                name_line = problems_file.readline()
                if(name_line == ''):
                    break
                problem = [list(problems_file.readline().strip()) for _ in range(9)]
                problem = [[int(e) for e in row] for row in problem]
                solution = sudoku(problem)
                self.checkIsValid(problem, solution)

if(__name__ == "__main__"):
    unittest.main()
