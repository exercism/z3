# Instructions

Implement a function using Z3's propositional logic capabilities to 
recreate the following propositional logic properties:

1. A & B == (A' | B')' (DeMorgan's Law)
2. [A -> (A -> B)] -> (A -> B)
3. A & (B' -> A') -> B

The function should return the three theorems written in Z3 notation.  The 
test cases will pass Not(A) and Not(B), Not(A) and B, A and Not(B), and A and 
B in four separate pairs to the created function.

For reference, the basic propositional logic functions in Z3 are:

And(A, B) = A & B

Or(A, B) = A | B

Not(A) = A'

Implies(A, B) = A -> B

(A == B) = (A = B)

Use the prove() function to confirm the accuracy of your theorems.  Z3 uses 
extensive test cases to prove theorems passed to this function, and will provide a counterexample
if the theorem is not sound.

Return the three theorems, in order, at the end of the function.  The order is important, 
as the test case file will compare results starting with the first theorem and ending with the third.