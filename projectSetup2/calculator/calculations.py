#from typing import List, Tuple, Union

#class Calculator:
  #  """A calculator class that performs basic operations and keeps history."""

   # _history: List[Tuple[str, Union[int, float]]] = []

    #@staticmethod
    #def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
     #   """Returns the sum of two numbers."""
      #  result = a + b
       # Calculator._add_to_history("add", result)
        #return result

    #@staticmethod
   #def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    #   """Returns the difference of two numbers."""
     #  result = a - b
      # Calculator._add_to_history("subtract", result)
       #return result

   #@staticmethod
    #def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
     #   """Returns the product of two numbers."""
      #  result = a * b
       # Calculator._add_to_history("multiply", result)
        #return result

    #@staticmethod
    #def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
     #   """Returns the quotient of two numbers. Raises exception if dividing by zero."""
      #  if b == 0:
       #     raise ZeroDivisionError("Cannot divide by zero.")
        #result = a / b
        #Calculator._add_to_history("divide", result)
        #return result

    #@classmethod
    #def _add_to_history(cls, operation: str, result: Union[int, float]) -> None:
     #   """Stores the operation and result in history."""
      #  cls._history.append((operation, result))

#    @classmethod
 #   def get_last_calculation(cls) -> Tuple[str, Union[int, float]]:
  #      """Returns the last calculation from history."""
   #     if not cls._history:
    #        raise ValueError("No calculations in history.")
     #   return cls._history[-1]

    #@classmethod
    #def clear_history(cls) -> None:
     #   """Clears the calculation history."""
      #  cls._history.clear()

# calculator/calculations.py
from calculator.operations import Operations

class Calculation:
    """Handles individual calculations."""
    
    def __init__(self, operation: str, a: float, b: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = self._perform_operation()

    def _perform_operation(self) -> float:
        """Executes the requested operation and returns the result."""
        operations_map = {
            "add": Operations.add,
            "subtract": Operations.subtract,
            "multiply": Operations.multiply,
            "divide": Operations.divide
        }
        return operations_map[self.operation](self.a, self.b)

    def __repr__(self) -> str:
        """Returns a string representation of the calculation."""
        return f"{self.a} {self.operation} {self.b} = {self.result}"
