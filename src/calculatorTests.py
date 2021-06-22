import unittest
from calculator import Calculator

class CalculatorTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        system = Calculator()
        self.assertIsInstance(system, Calculator)




if __name__ == '__main__':
    unittest.main()