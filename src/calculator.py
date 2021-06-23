
class Calculator:
    result = 0

    def __init__(self):
        pass

    @staticmethod
    def addition(a,b):
        c = a + b
        return c

    def add(self, a, b):
        self.result = self.addition(a,b)
        return self.result




