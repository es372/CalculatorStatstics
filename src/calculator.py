import math

class Calculator:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def addition(a,b):
        c = a + b
        return c

    @staticmethod
    def subtraction(a, b):
        c = a - b
        return c

    @staticmethod
    def multiplication(a, b):
        c = a * b
        return c

    @staticmethod
    def division(a,b):
        c = a/b
        return c

    @staticmethod
    def squaring(a):
        c = a**2
        return c

    @staticmethod
    def square_root(a):
        c = math.sqrt(a)
        return c



    def add(self, a, b):
        self.result = self.addition(a,b)
        return self.result

    def subtract(self, a, b):
        self.result = self.subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = self.multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = self.division(a, b)
        return self.result

    def square(self, a):
        self.result = self.squaring(a)
        return self.result

    def sqrt(self, a):
        self.result = self.square_root(a)
        return self.result




