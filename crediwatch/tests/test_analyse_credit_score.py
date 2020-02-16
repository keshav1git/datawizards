import unittest
from businessModels import analyse_loan_credibility


class TestBaseScore(unittest.TestCase):

    def test_score(self):
        dummy_xfactors = {"x1": 1, "x2": 3, "x3": 4, "x4": 5, "x5": 6}
        actual_base_score = analyse_loan_credibility.get_base_score(dummy_xfactors)
        self.assertEqual(actual_base_score, 26.466)

    def test_high_score(self):
        dummy_xfactors = {"x1": 155, "x2": 33, "x3": 34, "x4":35, "x5":67}
        actual_base_score = analyse_loan_credibility.get_base_score(dummy_xfactors)
        self.assertEqual(round(actual_base_score,3), round(329.01199999999994,3))

    def test_low_score(self):
        dummy_xfactors = {"x1":0.1, "x2":0.33, "x3":0.34, "x4":0.35, "x5":1}
        actual_base_score = analyse_loan_credibility.get_base_score(dummy_xfactors)
        print(actual_base_score)
        self.assertEqual(round(actual_base_score,3), round(2.57981,3))