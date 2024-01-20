#!/usr/bin/python3

"""
This is a sample Python code adhering to PEP 8 style guidelines
"""

class Calculator:
    """A simple calculator class."""

    def __init__(self):
        """Initialize the calculator."""
        self.result = 0

    def add(self, a, b):
        """Add two numbers."""
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        """Subtract b from a."""
        self.result = a - b
        return self.result

# Add more functions and classes as needed

def main():
    """Main function to demonstrate the code."""
    calculator = Calculator()

    # Perform some calculations
    result_sum = calculator.add(5, 3)
    result_difference = calculator.subtract(10, 4)

    print(f"Sum: {result_sum}")
    print(f"Difference: {result_difference}")


if __name__ == "__main__":
    main()

