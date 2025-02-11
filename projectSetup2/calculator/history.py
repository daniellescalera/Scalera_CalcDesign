#from typing import List, Tuple, Union

#class History:
 #   """A class to store and retrieve calculation history."""

  #  _history: List[Tuple[str, Union[int, float]]] = []

   # @classmethod
    #def add_to_history(cls, operation: str, result: Union[int, float]) -> None:
     #   """Stores the operation and result in history."""
      #  cls._history.append((operation, result))

    #@classmethod
    #def get_last_calculation(cls) -> Tuple[str, Union[int, float]]:
     #   """Returns the last calculation from history."""
      #  if not cls._history:
       #     raise ValueError("No calculations in history.")
        #return cls._history[-1]

    #@classmethod
    #def get_history(cls) -> List[Tuple[str, Union[int, float]]]:
     #   """Returns the full history of calculations."""
      #  return cls._history.copy()

    #@classmethod
    #def clear_history(cls) -> None:
     #   """Clears the calculation history."""
      #  cls._history.clear()

# calculator/history.py
from typing import List
from calculator.calculations import Calculation

class CalculationHistory:
    """Manages history of calculations."""
    _history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Stores a calculation in history."""
        cls._history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """Returns the last calculation performed."""
        if cls._history:
            return cls._history[-1]
        return None

    @classmethod
    def clear_history(cls):
        """Clears all calculation history."""
        cls._history.clear()
