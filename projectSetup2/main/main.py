#from calculator.calculations import Calculator

#def main():
 #   """Command-line interface for the Calculator."""
  #  print("Welcome to the Python Calculator!")
   # print("Available operations: add, subtract, multiply, divide")
    #print("Type 'history' to view past calculations, or 'exit' to quit.")

    #while True:
     #   user_input = input("\nEnter operation (or 'exit'): ").strip().lower()
        
      #  if user_input == "exit":
       #     print("Goodbye!")
        #    break
        #elif user_input == "history":
         #   history = Calculator.get_history()
          #  if history:
           #     print("\nCalculation History:")
            #    for operation, result in history:
             #       print(f"{operation}: {result}")
            #else:
             #   print("\nNo calculations in history.")
            #continue

        #if user_input not in ["add", "subtract", "multiply", "divide"]:
         #   print("Invalid operation! Please enter a valid operation.")
          #  continue

        #try:
         #   num1 = float(input("Enter first number: "))
          #  num2 = float(input("Enter second number: "))

           # if user_input == "add":
            #    result = Calculator.add(num1, num2)
            #elif user_input == "subtract":
            #    result = Calculator.subtract(num1, num2)
            #elif user_input == "multiply":
            #    result = Calculator.multiply(num1, num2)
            #elif user_input == "divide":
             #   result = Calculator.divide(num1, num2)

            #print(f"Result: {result}")

        #except ValueError:
         #   print("Invalid input! Please enter numeric values.")
        #except ZeroDivisionError:
         #   print("Error: Cannot divide by zero.")

#if __name__ == "__main__":
 #   main()

# main/main.py
from calculator.calculations import Calculation
from calculator.history import CalculationHistory

def main():
    """Main function to interact with the calculator."""
    while True:
        print("\nSimple Calculator")
        print("Choose operation: add, subtract, multiply, divide")
        print("Type 'exit' to quit.")

        operation = input("Enter operation: ").strip().lower()
        if operation == "exit":
            break
        if operation not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            calculation = Calculation(operation, a, b)
            CalculationHistory.add_calculation(calculation)

            print(f"Result: {calculation.result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main()
