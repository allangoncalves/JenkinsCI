from calculator import Calculator
import pytest


class TestCalculator():

    def __init__(self):
        self.calculator = Calculator()

    def test_add(self):
        assert 8 == self.calculator.add(3, 5)

    def test_sub(self):
        assert -1 == self.calculator.sub(1, 2)

    def test_add_type(self):
        with pytest.raises(NotImplementedError):
            self.calculator.add("a", "b")

    def test_sub_type(self):
        with pytest.raises(NotImplementedError):
            self.calculator.sub([1, 2], [3, 4])
