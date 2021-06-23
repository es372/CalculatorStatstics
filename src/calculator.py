
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







