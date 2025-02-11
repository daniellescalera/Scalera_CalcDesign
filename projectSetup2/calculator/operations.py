"""##def add(a,b):
  #  return a + b 

#def subtract(a,b):
 #   return a - b

#def multiply(a,b):
 #   return a * b

#def divide(a,b):
 #   return a / b

 calculator/operations.py """
class Operations:
    """Performs basic arithmetic operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Returns the difference between two numbers."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Returns the product of two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Returns the quotient of two numbers. Raises error on divide by zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
