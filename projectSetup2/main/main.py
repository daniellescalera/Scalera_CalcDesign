"""importing all of the needed commands"""
from calculator.calculations import Calculation
from calculator.history import CalculationHistory
from calculator import Calculator
def main():
    calculator = Calculator()  # Initialize the Calculator class with command handler
    calculator.start()

    while True:
        print("\nSimple Calculator")
        print("Choose operation: add, subtract, multiply, divide")
        print("Or use commands: greet, goodbye, exit, or menu")
        print("Type 'exit' to quit.")

        user_input = input("Enter operation or command: ").strip().lower()

        # Check if the input is a command
        if user_input in ["greet", "goodbye", "exit"]:
            calculator.command_handler.execute_command(user_input)
            if user_input == "exit":
                break
            continue

        # Handle arithmetic operations
        if user_input not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            calculation = Calculation(user_input, a, b)
            CalculationHistory.add_calculation(calculation)

            print(f"Result: {calculation.result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main()
