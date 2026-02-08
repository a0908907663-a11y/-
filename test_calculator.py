# test_calculator.py
# This file contains unit tests for the calculator functions

import unittest          # Import the unittest module
import calculator        # Import the calculator file


class TestCalculator(unittest.TestCase):
    # This class tests all calculator operations

    def test_add(self):
        # Test addition function
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        # Test subtraction function
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_multiply(self):
        # Test multiplication function
        self.assertEqual(calculator.multiply(4, 3), 12)

    def test_divide(self):
        # Test division function
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_divide_by_zero(self):
        # Test division by zero
        # The function should raise a ValueError
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)


# This block runs the tests when the file is executed
if __name__ == "__main__":
    unittest.main()
