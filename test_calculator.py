"""
Blackbox Testing Test Cases for Calculator Application
Author: Huzaifa
Date: December 2025
Test Strategy: Functional blackbox testing without knowledge of internal implementation
"""

import unittest
import sys
from calculator import Calculator


class TestCalculatorAddition(unittest.TestCase):
    """Test cases for addition functionality."""
    
    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        result = self.calc.add(-5, -3)
        self.assertEqual(result, -8)
    
    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        result = self.calc.add(10, -5)
        self.assertEqual(result, 5)
    
    def test_add_zero(self):
        """Test adding with zero."""
        result = self.calc.add(5, 0)
        self.assertEqual(result, 5)
    
    def test_add_two_zeros(self):
        """Test adding two zeros."""
        result = self.calc.add(0, 0)
        self.assertEqual(result, 0)
    
    def test_add_decimal_numbers(self):
        """Test adding decimal numbers."""
        result = self.calc.add(2.5, 3.5)
        self.assertEqual(result, 6.0)
    
    def test_add_large_numbers(self):
        """Test adding large numbers."""
        result = self.calc.add(1000000, 2000000)
        self.assertEqual(result, 3000000)


class TestCalculatorSubtraction(unittest.TestCase):
    """Test cases for subtraction functionality."""
    
    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = Calculator()
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        result = self.calc.subtract(10, 3)
        self.assertEqual(result, 7)
    
    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        result = self.calc.subtract(-5, -3)
        self.assertEqual(result, -2)
    
    def test_subtract_resulting_negative(self):
        """Test subtraction resulting in negative number."""
        result = self.calc.subtract(3, 10)
        self.assertEqual(result, -7)
    
    def test_subtract_zero(self):
        """Test subtracting zero."""
        result = self.calc.subtract(5, 0)
        self.assertEqual(result, 5)
    
    def test_subtract_from_zero(self):
        """Test subtracting from zero."""
        result = self.calc.subtract(0, 5)
        self.assertEqual(result, -5)
    
    def test_subtract_decimal_numbers(self):
        """Test subtracting decimal numbers."""
        result = self.calc.subtract(5.5, 2.5)
        self.assertEqual(result, 3.0)
    
    def test_subtract_same_numbers(self):
        """Test subtracting same numbers (should be zero)."""
        result = self.calc.subtract(5, 5)
        self.assertEqual(result, 0)


class TestCalculatorMultiplication(unittest.TestCase):
    """Test cases for multiplication functionality."""
    
    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = Calculator()
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        result = self.calc.multiply(4, 5)
        self.assertEqual(result, 20)
    
    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        result = self.calc.multiply(-4, -5)
        self.assertEqual(result, 20)
    
    def test_multiply_positive_and_negative(self):
        """Test multiplying positive and negative numbers."""
        result = self.calc.multiply(4, -5)
        self.assertEqual(result, -20)
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        result = self.calc.multiply(5, 0)
        self.assertEqual(result, 0)
    
    def test_multiply_by_one(self):
        """Test multiplying by one."""
        result = self.calc.multiply(5, 1)
        self.assertEqual(result, 5)
    
    def test_multiply_decimal_numbers(self):
        """Test multiplying decimal numbers."""
        result = self.calc.multiply(2.5, 4)
        self.assertEqual(result, 10.0)
    
    def test_multiply_large_numbers(self):
        """Test multiplying large numbers."""
        result = self.calc.multiply(1000, 2000)
        self.assertEqual(result, 2000000)


class TestCalculatorDivision(unittest.TestCase):
    """Test cases for division functionality."""
    
    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = Calculator()
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        result = self.calc.divide(20, 4)
        self.assertEqual(result, 5)
    
    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        result = self.calc.divide(-20, -4)
        self.assertEqual(result, 5)
    
    def test_divide_positive_by_negative(self):
        """Test dividing positive by negative."""
        result = self.calc.divide(20, -4)
        self.assertEqual(result, -5)
    
    def test_divide_by_one(self):
        """Test dividing by one."""
        result = self.calc.divide(10, 1)
        self.assertEqual(result, 10)
    
    def test_divide_decimal_result(self):
        """Test division resulting in decimal."""
        result = self.calc.divide(10, 4)
        self.assertEqual(result, 2.5)
    
    def test_divide_by_zero_raises_exception(self):
        """Test that dividing by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        result = self.calc.divide(0, 5)
        self.assertEqual(result, 0)


class TestCalculatorSquare(unittest.TestCase):
    """Test cases for square functionality."""
    
    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = Calculator()
    
    def test_square_positive_number(self):
        """Test squaring a positive number."""
        result = self.calc.square(5)
        self.assertEqual(result, 25)
    
    def test_square_negative_number(self):
        """Test squaring a negative number."""
        result = self.calc.square(-5)
        self.assertEqual(result, 25)
    
    def test_square_zero(self):
        """Test squaring zero."""
        result = self.calc.square(0)
        self.assertEqual(result, 0)
    
    def test_square_one(self):
        """Test squaring one."""
        result = self.calc.square(1)
        self.assertEqual(result, 1)
    
    def test_square_decimal_number(self):
        """Test squaring a decimal number."""
        result = self.calc.square(2.5)
        self.assertAlmostEqual(result, 6.25, places=5)


class TestCalculatorSquareRoot(unittest.TestCase):
    """Test cases for square root functionality."""
    
    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = Calculator()
    
    def test_square_root_perfect_square(self):
        """Test square root of a perfect square."""
        result = self.calc.square_root(16)
        self.assertEqual(result, 4.0)
    
    def test_square_root_zero(self):
        """Test square root of zero."""
        result = self.calc.square_root(0)
        self.assertEqual(result, 0.0)
    
    def test_square_root_one(self):
        """Test square root of one."""
        result = self.calc.square_root(1)
        self.assertEqual(result, 1.0)
    
    def test_square_root_decimal_result(self):
        """Test square root resulting in decimal."""
        result = self.calc.square_root(2)
        self.assertAlmostEqual(result, 1.414, places=3)
    
    def test_square_root_negative_raises_exception(self):
        """Test that square root of negative raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.square_root(-5)
    
    def test_square_root_large_number(self):
        """Test square root of large number."""
        result = self.calc.square_root(10000)
        self.assertEqual(result, 100.0)


class TestCalculatorPower(unittest.TestCase):
    """Test cases for power functionality."""
    
    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = Calculator()
    
    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)
    
    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        result = self.calc.power(5, 0)
        self.assertEqual(result, 1)
    
    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        result = self.calc.power(2, -1)
        self.assertEqual(result, 0.5)
    
    def test_power_one_base(self):
        """Test power with base 1."""
        result = self.calc.power(1, 5)
        self.assertEqual(result, 1)
    
    def test_power_zero_base(self):
        """Test power with base 0."""
        result = self.calc.power(0, 5)
        self.assertEqual(result, 0)
    
    def test_power_decimal_base(self):
        """Test power with decimal base."""
        result = self.calc.power(2.5, 2)
        self.assertAlmostEqual(result, 6.25, places=5)


class TestCalculatorClear(unittest.TestCase):
    """Test cases for clear functionality."""
    
    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = Calculator()
    
    def test_clear_resets_result(self):
        """Test that clear resets the result."""
        self.calc.add(5, 5)
        result = self.calc.clear()
        self.assertEqual(result, 0)
    
    def test_get_result_after_clear(self):
        """Test getting result after clear."""
        self.calc.add(10, 5)
        self.calc.clear()
        result = self.calc.get_result()
        self.assertEqual(result, 0)


class TestCalculatorResultPersistence(unittest.TestCase):
    """Test cases for result persistence."""
    
    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = Calculator()
    
    def test_get_result_returns_last_operation(self):
        """Test that get_result returns the last operation result."""
        self.calc.add(3, 4)
        result = self.calc.get_result()
        self.assertEqual(result, 7)
    
    def test_result_persists_between_operations(self):
        """Test that result persists after operation."""
        self.calc.multiply(5, 2)
        result1 = self.calc.get_result()
        result2 = self.calc.get_result()
        self.assertEqual(result1, result2)
        self.assertEqual(result1, 10)


class TestCalculatorIntegration(unittest.TestCase):
    """Integration tests combining multiple operations."""
    
    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = Calculator()
    
    def test_multiple_operations_sequence(self):
        """Test performing multiple operations in sequence."""
        self.calc.add(10, 5)
        self.assertEqual(self.calc.get_result(), 15)
        
        self.calc.multiply(self.calc.get_result(), 2)
        self.assertEqual(self.calc.get_result(), 30)
        
        self.calc.divide(self.calc.get_result(), 3)
        self.assertEqual(self.calc.get_result(), 10)
    
    def test_clear_between_operations(self):
        """Test clearing between operations."""
        self.calc.add(5, 5)
        self.calc.clear()
        result = self.calc.subtract(10, 3)
        self.assertEqual(result, 7)


if __name__ == '__main__':
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    test_result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("TEST EXECUTION SUMMARY")
    print("="*70)
    print(f"Tests Run: {test_result.testsRun}")
    print(f"Successes: {test_result.testsRun - len(test_result.failures) - len(test_result.errors)}")
    print(f"Failures: {len(test_result.failures)}")
    print(f"Errors: {len(test_result.errors)}")
    print("="*70)
