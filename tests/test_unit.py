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


    class TestCalculator():
        
        @pytest.mark.parametrize("a, b, expected", [
            (9, -5, 4),
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0)
        ])

        def test_add(self, a, b, expected):
            # Arrange
            calculator = CalculatorHelper()
            # Action
            value = calculator.add(a, b)
            # Assert
            assert value == expected, f"Expected {a} + {b} to be {expected}, but got {value}"


        def test_subtract(self):
            # Arrange
            calculator = CalculatorHelper()
            # Action
            value = calculator.subtract(1,1)
            # Assert
            assert value == 0, "Expected result to be 0"
        
        def test_divide(self):
            # Arrange
            calculator = CalculatorHelper()
            # Action
            value = calculator.divide(10,2)
            # Assert
            assert value == 5, "Expected result to be 5"

        def test_multiply(self):
            # Arrange
            calculator = CalculatorHelper()
            # Action
            value = calculator.multiply(1,1)
            # Assert
            assert value == 1, "Expected result to be 1"

        def test_div_by_zero(self):
            with pytest.raises(ZeroDivisionError):
                1 / 0

            #my_name = "Scott"
            #assert_that(value).is_equal_to(2)
            #assert_that(my_name).is_length(5).starts_with("S").ends_with("tt")
