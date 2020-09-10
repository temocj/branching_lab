import unittest, random, pdb

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    def setUp(self):
        self.scores = [30, 91, 52, 99, 19, 74, 88, 78, 48, 34,\
                       32, 77,  6, 92,  7,  1, 51, 86, 72, 28]

    # Tests

    # Test latest score (the last thing in the list)
    @unittest.skip
    def test_latest(self):
        actual = latest(self.scores)
        self.assertEqual(28, actual)

    # Test personal best (the highest score in the list)
    @unittest.skip
    def test_best(self):
        actual = personal_best(self.scores)
        self.assertEqual(99, actual)

    # Test top three from list of scores
    @unittest.skip
    def test_personal_top_three(self):
        actual = personal_top_three(self.scores)
        self.assertIn(99, actual)
        self.assertIn(92, actual)
        self.assertIn(91, actual)

    # Test ordered from highest tp lowest
    @unittest.skip
    def test_personal_top_three(self):
        actual = personal_top_three(self.scores)
        self.assertEqual([99, 92, 91], actual)

    # Test top three when there is a tie
    @unittest.skip
    def test_personal_top_three__tie(self):
        actual = latest(self.scores + [99])
        self.assertEqual([99, 99, 92], actual)

    # Test top three when there are less than three
    @unittest.skip
    def test_personal_top_three__less_than_three(self):
        actual = latest(self.scores[:2])
        self.assertEqual([91, 30], actual)

    # Test top three when there is only one
    @unittest.skip
    def test_personal_top_three__only_one(self):
        actual = personal_top_three([5])
        self.assertEqual([5], actual)
