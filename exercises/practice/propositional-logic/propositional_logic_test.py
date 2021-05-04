import unittest
from z3 import *
from .propositional_logic import *

class PropositionalLogicTest(unittest.TestCase):
    def test_A_B(self):
        A, B = Bools('A B')
        t1, t2, t3 = propositional_logic_proofs(A, B)

        expected_t1 = And(A, B) == Not(Or(Not(A), Not(B)))
        expected_t2 = Implies(Implies(A, Implies(A, B)), Implies(A, B))
        expected_t3 = Implies(And(A, Implies(Not(B), Not(A))), B)

        self.assertEqual(t1, expected_t1)
        self.assertEqual(t2, expected_t2)
        self.assertEqual(t3, expected_t3)

    def test_notA_B(self):
        A, B = Bools('A B')
        t1, t2, t3 = propositional_logic_proofs(Not(A), B)
        expected_t1 = And(Not(A), B) == Not(Or(Not(Not(A)), Not(B)))
        expected_t2 = Implies(Implies(Not(A), Implies(Not(A), B)), Implies(Not(A), B))
        expected_t3 = Implies(And(Not(A), Implies(Not(B), Not(Not(A)))), B)

        self.assertEqual(t1, expected_t1)
        self.assertEqual(t2, expected_t2)
        self.assertEqual(t3, expected_t3)

    def test_A_notB(self):
        A, B = Bools('A B')
        t1, t2, t3 = propositional_logic_proofs(A, Not(B))
        expected_t1 = And(A, Not(B)) == Not(Or(Not(A), Not(Not(B))))
        expected_t2 = Implies(Implies(A, Implies(A, Not(B))), Implies(A, Not(B)))
        expected_t3 = Implies(And(A, Implies(Not(Not(B)), Not(A))), Not(B))

        self.assertEqual(t1, expected_t1)
        self.assertEqual(t2, expected_t2)
        self.assertEqual(t3, expected_t3)

    def test_notA_notB(self):
        A, B = Bools('A B')
        t1, t2, t3 = propositional_logic_proofs(Not(A), Not(B))
        expected_t1 = And(Not(A), Not(B)) == Not(Or(Not(Not(A)), Not(Not(B))))
        expected_t2 = Implies(Implies(Not(A), Implies(Not(A), Not(B))), Implies(Not(A), Not(B)))
        expected_t3 = Implies(And(Not(A), Implies(Not(Not(B)), Not(Not(A)))), Not(B))

        self.assertEqual(t1, expected_t1)
        self.assertEqual(t2, expected_t2)
        self.assertEqual(t3, expected_t3)

if __name__ == "__main__":
    unittest.main()
