class Calculator:
    
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        return self.result
    
    def square(self, a):
        self.result = a ** 2
        return self.result
    
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        import math
        self.result = math.sqrt(a)
        return self.result
    
    def clear(self):
        self.result = 0
        return self.result
    
    def get_result(self):
        return self.result
    
    def power(self, base, exponent):
        self.result = base ** exponent
        return self.result
