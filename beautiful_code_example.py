# This is a sample Python code adhering to PEP 8 style guidelines

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

    def multiply(self, a, b):
        """Multiply two numbers."""
        self.result = a * b
        return self.result

    def divide(self, a, b):
        """Divide a by b."""
        if b != 0:
            self.result = a / b
            return self.result
        else:
            raise ValueError("Cannot divide by zero")


def main():
    """Main function to demonstrate the code."""
    calculator = Calculator()

    # Perform some calculations
    result_sum = calculator.add(5, 3)
    result_difference = calculator.subtract(10, 4)
    result_product = calculator.multiply(2, 7)

    print(f"Sum: {result_sum}")
    print(f"Difference: {result_difference}")
    print(f"Product: {result_product}")

    try:
        # Attempt to divide by zero
        result_quotient = calculator.divide(8, 0)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

