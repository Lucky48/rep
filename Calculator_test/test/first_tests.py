import pytest
from app.calculator import Calculator


class TestCalc_pos:
    def setup(self):
        self.calc = Calculator

    def test_adding_calculation_positive(self):
        assert self.calc.addition(self, 2, 3) == 5

    def test_subtraction_calculation_positive(self):
        assert self.calc.subtraction(self, 3, 1) == 2

    def test_multiply_calculation_positive(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculation_positive(self):
        assert self.calc.division(self, 6, 2) == 3



class TestCalc_neg:
    def setup(self):
        self.calc = Calculator

    def test_adding_calculation_negative(self):
        assert self.calc.addition(self, 2, 3) == 6

    def test_subtraction_calculation_negative(self):
        assert self.calc.subtraction(self, 3, 1) == 3

    def test_multiply_calculation_negative(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculation_negative(self):
        assert self.calc.division(self, 6, 2) == 4
