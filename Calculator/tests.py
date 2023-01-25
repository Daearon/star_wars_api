import unittest
from mod_calc import *


class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(summation(0.25, 0.5), 0.75)

