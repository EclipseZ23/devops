from BE.calculator_helper import CalculatorHelper
from assertpy import assert_that
import pytest

class TestBase():

    @classmethod
    def setup_class(cls):
            """instantiate the CalculatorHelper once for all tests."""
            cls.calculator = CalculatorHelper()

    @classmethod
    def teardown_class(cls):
        """Teardown class method to clean up after all tests."""
        cls.calculator = None


class TestCalculator(TestBase):
    
    @pytest.mark.parametrize("a, b, expected", [
        (9, -5, 4),
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0)
    ])

    def test_add(self, a, b, expected):
        
        # Action
        value = self.calculator.add(a, b)
        # Assert
        assert value == expected, f"Expected {a} + {b} to be {expected}, but got {value}"


    def test_subtract(self):
    
        # Action
        value = self.calculator.subtract(1,1)
        # Assert
        assert value == 0, "Expected result to be 0"
    
    def test_divide(self):

        # Action
        value = self.calculator.divide(10,2)
        # Assert
        assert value == 5, "Expected result to be 5"

    def test_multiply(self):
      
        # Action
        value = self.calculator.multiply(1,1)
        # Assert
        assert value == 1, "Expected result to be 1"

    def test_div_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            pytest.mark.parametrize(self.calculator.divide(10,0))
