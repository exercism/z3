import unittest
from z3 import*
from bowling import bowlingScore

class BowlingScoreTest(unittest.TestCase):
    def test_all_zeros(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(bowlingScore(pins_per_roll), 0)

    def test_all_strikes(self):
        pins_per_roll = (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
        self.assertEqual(bowlingScore(pins_per_roll), 300)

    def test_tenth_frame_all_strikes(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10)
        self.assertEqual(bowlingScore(pins_per_roll), 30)

    def test_tenth_frame_first_two_strikes(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 2)
        self.assertEqual(bowlingScore(pins_per_roll), 22)

    def test_tenth_frame_first_one_strike(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2, 2)
        self.assertEqual(bowlingScore(pins_per_roll), 14)

    def test_tenth_frame_strike_spare(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2, 8)
        self.assertEqual(bowlingScore(pins_per_roll), 20)

    def test_tenth_frame_spare_strike(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 10)
        self.assertEqual(bowlingScore(pins_per_roll), 20)

    def test_tenth_frame_spare(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 6)
        self.assertEqual(bowlingScore(pins_per_roll), 16)

    def test_consecutive_strikes(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 5)
        self.assertEqual(bowlingScore(pins_per_roll), 65)

    def test_consecutive_strikes_followed_by_number(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 7, 1, 0, 0, 0, 5)
        self.assertEqual(bowlingScore(pins_per_roll), 88)

    def test_strike_strike_spare(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 5, 5, 0, 0, 0, 0, 0, 5)
        self.assertEqual(bowlingScore(pins_per_roll), 60)

    def test_strike_strike_spare_followed_by_number(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 5, 5, 7, 1, 0, 0, 0, 5)
        self.assertEqual(bowlingScore(pins_per_roll), 75)

    def test_consecutive_spares(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 2, 7, 4, 6, 0, 0, 0, 0, 0, 5)
        self.assertEqual(bowlingScore(pins_per_roll), 36)

    def test_consecutive_spares_followed_by_number(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 2, 7, 4, 6, 7, 1, 0, 0, 0, 5)
        self.assertEqual(bowlingScore(pins_per_roll), 51)

    def test_single_strike(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0)
        self.assertEqual(bowlingScore(pins_per_roll), 10)

    def test_single_strike_followed_by_number(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 5, 3, 0, 0, 0, 0)
        self.assertEqual(bowlingScore(pins_per_roll), 26)

    def test_single_spare(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 7, 0, 0, 0, 0, 0, 0)
        self.assertEqual(bowlingScore(pins_per_roll), 10)

    def test_single_spare_followed_by_number(self):
        pins_per_roll = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 7, 5, 3, 0, 0, 0, 0)
        self.assertEqual(bowlingScore(pins_per_roll), 23)

    def test_all_open_frames(self):
        pins_per_roll = (1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0)
        self.assertEqual(bowlingScore(pins_per_roll), 50)

    def test_all_open_frames(self):
        pins_per_roll = (5, 3, 8, 2, 3, 4, 8, 0, 10, 4, 4, 2, 6, 7, 2, 6, 1, 9, 0)
        self.assertEqual(bowlingScore(pins_per_roll), 95)

if __name__ == "__main__":
    unittest.main()