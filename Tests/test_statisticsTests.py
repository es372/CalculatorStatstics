import unittest
from Statistics.statistics import Statistics
from RNG.get_dataset import generate_sample
from Calculator.calculator import Calculator


class StatisticsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.testData = generate_sample(5, 0, 10)
        self.statistics = Statistics()
        self.Calculator = Calculator()

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_instantiate_data(self):
        self.assertIsInstance(self.testData, list)
        try:
            self.testData
        except IndexError:
            print('EmptyListError: list contains no data')

    def test_meanMethod(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 4.72)
        try:
            mean.division()
        except IndexError:
            print('DivideByZeroError: undefined or does not exist, 0 denominator')


    def test_modeMethod(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, 'Exception: Numbers in dataset have same frequency.')


if __name__ == '__main__':
    unittest.main()
