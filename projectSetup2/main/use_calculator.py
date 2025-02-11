from calculator.operations import Operations

# Perform calculations
print("Addition:", Operations.add(5, 3))
print("Subtraction:", Operations.subtract(10, 4))
print("Multiplication:", Operations.multiply(2, 6))
print("Division:", Operations.divide(8, 2))

# Handling division by zero
try:
    print("Division by Zero:", Operations.divide(5, 0))
except ZeroDivisionError as e:
    print("Error:", e)
