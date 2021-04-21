import unittest
from goldbach import goldbach

def tupleEqualNoOrder(t1: tuple, t2: tuple) -> bool:
    """Check if two two-element tuples have the same elements."""
    assert len(t1) == 2
    assert len(t2) == 2
    if(t1[0] == t2[0]):
        return t1[1] == t2[1]
    else:
        return t1[0] == t2[1] and t1[1] == t2[0]

class GoldbachTester(unittest.TestCase):
    def test_exclusive(self):
        cases = [(4, (2, 2)), (6, (3, 3)), (8, (5, 3)), (12, (5, 7))]
        for (even, primes) in cases:
            components = goldbach(even)
            self.assertIsNotNone(components, f"No factors returned for {even}.")
            self.assertCountEqual(primes, components, f"Expecting {primes} for {even} but got {components}")

    def test_non_exclusive(self):
        cases = [
            (10, [(5, 5), (7, 3)]),
            (30, [(13, 17), (11, 19), (7, 23)]),
            (52, [(47, 5), (41, 11)])
        ]
        for (even, primesList) in cases:
            components = goldbach(even)
            for primes in primesList:
                if(tupleEqualNoOrder(primes, components)):
                    self.assertTrue(True)
                    break
            else:
                self.assertTrue(False, f"No matching factor pair found for {even}. Factors returned: {components}")

if(__name__ == "__main__"):
    unittest.main()
