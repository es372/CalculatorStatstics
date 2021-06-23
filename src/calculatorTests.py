import unittest
from calculator import Calculator

class CalculatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.Calculator = Calculator()

    def test_instantiate_calculator(self):
        system = Calculator()
        self.assertIsInstance(system, Calculator)

    def test_addMethod(self):
        self.assertEqual(self.Calculator.add(2, 2), 4)
        self.assertEqual(self.Calculator.result, 4)



if __name__ == '__main__':
    unittest.main()