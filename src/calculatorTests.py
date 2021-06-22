import unittest
from calculator import calculator

class CalculatorTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        system = calculator()
        self.assertIsInstance(system, calculator)


if __name__ == '__main__':
    unittest.main()