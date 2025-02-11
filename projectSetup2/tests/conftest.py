#import pytest
#from calculator.history import History

#@pytest.fixture
#def clear_calculator_history():
 #   """Fixture to clear the calculator history before and after each test."""
  #  History.clear_history()  # Clear history before the test runs
   # yield  # Run the test
    #History.clear_history()  # Clear history after the test runs


# tests/conftest.py
import pytest
from calculator.calculations import Calculation
from calculator.history import CalculationHistory

@pytest.fixture
def sample_calculations():
    """Provides sample calculations for testing."""
    CalculationHistory.clear_history()
    CalculationHistory.add_calculation(Calculation("add", 3, 2))
    CalculationHistory.add_calculation(Calculation("multiply", 4, 2))
    return CalculationHistory
