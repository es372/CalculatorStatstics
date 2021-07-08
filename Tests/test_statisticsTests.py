import unittest
from Statistics.statistics import Statistics
from RNG.get_dataset import generate_sample


class StatisticsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.testData = generate_sample(5, 0, 10)
        self.statistics = Statistics()


    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_instantiate_data(self):
        self.assertIsInstance(self.testData, list)
        try:
            self.testData
        except IndexError:
            print('list contains no data')

    def test_meanMethod(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 4.72)

if __name__ == '__main__':
    unittest.main()
