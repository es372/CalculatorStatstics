import csv

class CsvReader:
    text_data = []
    int_values = []

    def __init__(self, filepath):
        with open(filepath) as csv_file:
            csv_data = csv.DictReader(csv_file)
            for row in csv_data:
                self.text_data.append(row)

    @staticmethod
    def integer_conversion(value1, value2, value3):
        data = [{'a' : int(value1), 'b' : int(value2), 'result' : int(value3)}]
        return data

    def return_data_as_integer(self):
        for row in self.text_data:
            self.int_values.append(self.integer_conversion(row['a'], row['b'], row['result']))

        return self.int_values