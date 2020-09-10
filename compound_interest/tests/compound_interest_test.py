import unittest, pdb

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    def setUp(self):
        pass

    # Tests

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_a(self):
        actual = CompoundInterest.calculate(100.00, 10.00, 20)
        self.assertEqual(732.81, actual)
    
    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_b(self):
            actual = CompoundInterest.calculate(100.00, 6.00, 10)
            self.assertEqual(181.94, actual)

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_c(self):
        actual = CompoundInterest.calculate(100000.00, 5.00, 8)
        self.assertEqual(149058.55, actual)

    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_zero_principal(self):
        actual = CompoundInterest.calculate(0.00, 10.00, 1)
        self.assertEqual(0.00, actual)

    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_zero_percent(self):
            actual = CompoundInterest.calculate(100.00, 0.00, 10)
            self.assertEqual(100.00, actual)

    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

