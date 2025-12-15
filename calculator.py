"""
Simple Calculator Application
This is a basic calculator that performs arithmetic operations.
Testing focus: Blackbox Testing
"""

class Calculator:
    """A simple calculator class that performs basic arithmetic operations."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.result = 0
    
    def add(self, a, b):
        """Add two numbers and return the result."""
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        """Subtract two numbers and return the result."""
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        """Divide two numbers and return the result."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        return self.result
    
    def square(self, a):
        """Return the square of a number."""
        self.result = a ** 2
        return self.result
    
    def square_root(self, a):
        """Return the square root of a number."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        import math
        self.result = math.sqrt(a)
        return self.result
    
    def clear(self):
        """Clear the result."""
        self.result = 0
        return self.result
    
    def get_result(self):
        """Get the current result."""
        return self.result
    
    def power(self, base, exponent):
        """Calculate base raised to the power of exponent."""
        self.result = base ** exponent
        return self.result
