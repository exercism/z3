import unittest
from z3 import*
from bowling import bowlingScore

class BowlingScoreTest(unittest.TestCase):
    def check(self, pins_per_roll: tuple, expected_score: int):
        """Checks the inputs for a case with an expected output and prints a helpful message upon failure."""
        score = bowlingScore(pins_per_roll)
        self.assertEqual(score, expected_score,
                         f"Error: Got a score of {score} instead of the correct{expected_score} for rolls {pins_per_roll}")

    def test_all_zeros(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0)

    def test_all_strikes(self):
        self.check((10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10), 300)

    def test_tenth_frame_all_strikes(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10), 30)

    def test_tenth_frame_first_two_strikes(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 2), 22)

    def test_tenth_frame_first_one_strike(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2, 2), 14)

    def test_tenth_frame_strike_spare(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2, 8), 20)

    def test_tenth_frame_spare_strike(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 10), 20)

    def test_tenth_frame_spare(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 6), 16)

    def test_consecutive_strikes(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 5), 65)

    def test_consecutive_strikes_followed_by_number(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 7, 1, 0, 0, 0, 5), 88)

    def test_strike_strike_spare(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 5, 5, 0, 0, 0, 0, 0, 5), 60)

    def test_strike_strike_spare_followed_by_number(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 5, 5, 7, 1, 0, 0, 0, 5), 75)

    def test_consecutive_spares(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 2, 7, 4, 6, 0, 0, 0, 0, 0, 5), 36)

    def test_consecutive_spares_followed_by_number(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 2, 7, 4, 6, 7, 1, 0, 0, 0, 5), 51)

    def test_single_strike(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0), 10)

    def test_single_strike_followed_by_number(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 5, 3, 0, 0, 0, 0), 26)

    def test_single_spare(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 7, 0, 0, 0, 0, 0, 0), 10)

    def test_single_spare_followed_by_number(self):
        self.check((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 7, 5, 3, 0, 0, 0, 0), 23)

    def test_all_open_frames(self):
        self.check((1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0), 50)

    def test_all_open_frames(self):
        self.check((5, 3, 8, 2, 3, 4, 8, 0, 10, 4, 4, 2, 6, 7, 2, 6, 1, 9, 0), 95)

if __name__ == "__main__":
    unittest.main()
