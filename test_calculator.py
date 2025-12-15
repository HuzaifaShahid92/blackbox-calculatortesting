import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)
    
    def test_add_negative(self):
        result = self.calc.add(-5, -3)
        self.assertEqual(result, -8)
    
    def test_subtract(self):
        result = self.calc.subtract(10, 3)
        self.assertEqual(result, 7)
    
    def test_subtract_negative(self):
        result = self.calc.subtract(3, 10)
        self.assertEqual(result, -7)
    
    def test_multiply(self):
        result = self.calc.multiply(4, 5)
        self.assertEqual(result, 20)
    
    def test_multiply_zero(self):
        result = self.calc.multiply(5, 0)
        self.assertEqual(result, 0)
    
    def test_divide(self):
        result = self.calc.divide(20, 4)
        self.assertEqual(result, 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_square(self):
        result = self.calc.square(5)
        self.assertEqual(result, 25)
    
    def test_square_root(self):
        result = self.calc.square_root(16)
        self.assertEqual(result, 4.0)
    
    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            self.calc.square_root(-5)
    
    def test_power(self):
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)
    
    def test_clear(self):
        self.calc.add(5, 5)
        result = self.calc.clear()
        self.assertEqual(result, 0)
    
    def test_get_result(self):
        self.calc.add(3, 4)
        result = self.calc.get_result()
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
