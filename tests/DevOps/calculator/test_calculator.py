import unittest
from DevOps.calculator import calculator

class TestCalculator(unittest.TestCase):
    def test_add_number(self):
        assert calculator.add_number(1, 2) == 3
    
    def test_sub_number(self):
        assert calculator.sub_number(2, 1) == 1

    def test_div_number(self):
        assert calculator.div_number(5, 2) == 2
    
    def test_sub_number(self):
        assert calculator.mul_number(2, 3) == 6