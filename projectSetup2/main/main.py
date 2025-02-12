# main/main.py
from calculator.calculations import Calculation
from calculator.history import CalculationHistory

def main():
    #Main function to interact with the calculator.
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
