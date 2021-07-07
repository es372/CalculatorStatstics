import unittest
from CsvReader.csvReader import CsvReader
from Calculator.calculator import Calculator

class CalculatorCsvTest(unittest.TestCase):

    def setUp(self) -> None:
        self.Calculator = Calculator()

    def test_csvReader_addition(self):
        self.csv_reader = CsvReader('./Data(CSV)/addition.csv')
        data = self.csv_reader.return_data_as_integer()
        for row in data:
            self.assertEqual(self.Calculator.add(row['a'], row['b']), row['result'])

    def test_csvReader_subtraction(self):
        self.csv_reader = CsvReader('./Data(CSV)/subtraction.csv')
        data = self.csv_reader.return_data_as_integer()
        for row in data:
            self.assertEqual(self.Calculator.subtract(row['a'], row['b']), row['result'])

    def test_csvReader_multiplication(self):
        self.csv_reader = CsvReader('./Data(CSV)/multiplication.csv')
        data = self.csv_reader.return_data_as_integer()
        for row in data:
            self.assertEqual(self.Calculator.multiply(row['a'], row['b']), row['result'])

    def test_csvReader_division(self):
        self.csv_reader = CsvReader('./Data(CSV)/division.csv')
        data = self.csv_reader.return_data_as_integer()
        for row in data:
            self.assertEqual(self.Calculator.divide(row['a'], row['b']), row['result'])

    def test_csvReader_squaring(self):
        self.csv_reader = CsvReader('./Data(CSV)/square.csv')
        data = self.csv_reader.return_data_as_integer()
        for row in data:
            self.assertEqual(self.Calculator.square(row['a']), row['result'])

    def test_csvReader_sqrt(self):
        self.csv_reader = CsvReader('./Data(CSV)/square_root.csv')
        data = self.csv_reader.return_data_as_integer()
        for row in data:
            self.assertEqual(self.Calculator.sqrt(row['a']), row['result'])

if __name__ == '__main__':
    unittest.main()



