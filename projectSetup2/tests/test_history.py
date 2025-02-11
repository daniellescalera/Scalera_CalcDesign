"""import pytest
from calculator.history import History

def test_history_tracking():
    #Test adding and retrieving history entries.
    History.add_to_history("add", 5)
    History.add_to_history("multiply", 10)

    assert History.get_last_calculation() == ("multiply", 10)
    assert History.get_history() == [("add", 5), ("multiply", 10)]

def test_clear_history():
    #Test clearing the calculation history.
    History.add_to_history("subtract", 3)
    assert len(History.get_history()) > 0

    History.clear_history()
    assert History.get_history() == []

    with pytest.raises(ValueError, match="No calculations in history."):
        History.get_last_calculation() """

# tests/test_history.py
from calculator.history import CalculationHistory
from calculator.calculations import Calculation

def test_add_and_retrieve_calculation(sample_calculations):
    """Test storing and retrieving calculations."""
    last_calc = sample_calculations.get_last_calculation()
    assert last_calc is not None
    assert last_calc.operation == "multiply"
    assert last_calc.result == 8

def test_clear_history(sample_calculations):
    """Test clearing history."""
    sample_calculations.clear_history()
    assert sample_calculations.get_last_calculation() is None
