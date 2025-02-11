"""import pytest
from calculator.calculations import Calculator

def test_addition(clear_calculator_history):
    assert Calculator.add(2, 2) == 4
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0.5, 0.5) == 1.0

def test_subtraction(clear_calculator_history):
    assert Calculator.subtract(2, 2) == 0
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(0, 5) == -5

def test_multiplication(clear_calculator_history):
    assert Calculator.multiply(3, 3) == 9
    assert Calculator.multiply(-2, 3) == -6
    assert Calculator.multiply(0, 10) == 0

def test_division(clear_calculator_history):
    assert Calculator.divide(6, 2) == 3
    assert Calculator.divide(5, 2) == 2.5
    assert Calculator.divide(-6, 3) == -2

    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        Calculator.divide(5, 0)

def test_history(clear_calculator_history):
    Calculator.add(1, 1)
    Calculator.multiply(2, 2)
    assert Calculator.get_last_calculation() == ("multiply", 4)

    Calculator.clear_history()
    with pytest.raises(ValueError, match="No calculations in history."):
        Calculator.get_last_calculation()"""

# tests/test_calculations.py
import pytest
from calculator.calculations import Calculation
from calculator.operations import Operations

def test_operations():
    """Test basic operations."""
    assert Operations.add(2, 3) == 5
    assert Operations.subtract(5, 3) == 2
    assert Operations.multiply(3, 3) == 9
    assert Operations.divide(10, 2) == 5

def test_zero_division():
    """Test division by zero exception."""
    with pytest.raises(ZeroDivisionError):
        Operations.divide(5, 0)

def test_calculation():
    """Test calculation wrapper."""
    calc = Calculation("add", 2, 3)
    assert calc.result == 5
    calc = Calculation("multiply", 2, 3)
    assert calc.result == 6
