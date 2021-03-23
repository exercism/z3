from z3 import *


def propositional_logic_proofs(A, B):
    # Recreate the first theorem A & B == (A' | B')' (DeMorgan's Law) using Z3's propositional logic functions.
    theorem_one = And(A, B) == Not(Or(Not(A), Not(B)))

    # Recreate the second theorem [A -> (A -> B)] -> (A -> B).
    theorem_two = Implies(Implies(A, Implies(A, B)),Implies(A, B))

    # Recreate the third theorem A & (B' -> A') -> B.
    theorem_three = Implies(And(A, Implies(Not(B), Not(A))), B)

    return theorem_one, theorem_two, theorem_three
