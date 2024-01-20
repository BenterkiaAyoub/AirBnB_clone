#!/usr/bin/python3

"""
Test cases for the example.py code
"""

import unittest
from example import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""

    def test_add(self):
        """Test add method."""
        calculator = Calculator()
        result = calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        """Test subtract method."""
        calculator = Calculator()
        result = calculator.subtract(7, 2)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()

