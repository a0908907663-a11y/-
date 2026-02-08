# calculator.py
# This file contains simple calculator functions

def add(a, b):
    # This function returns the sum of two numbers
    return a + b


def subtract(a, b):
    # This function returns the difference between two numbers
    return a - b


def multiply(a, b):
    # This function returns the product of two numbers
    return a * b


def divide(a, b):
    # This function returns the division of two numbers
    # It raises an error if the second number is zero
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


# This block runs only if the file is executed directly
if __name__ == "__main__":
    # Read the first number from the user
    x = float(input("Enter the first number: "))

    # Read the second number from the user
    y = float(input("Enter the second number: "))

    # Print calculation results
    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))
