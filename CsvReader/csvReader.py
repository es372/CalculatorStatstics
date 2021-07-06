import csv
from pathlib import Path

class CsvReader:
    text_data = []

    def __init__(self, filepath):
        self.text_data = []
        relative = Path(filepath)
        absolute = relative.absolute()
        with open(absolute) as csv_file:
            csv_data = csv.DictReader(csv_file)
            for row in csv_data:
                self.text_data.append(row)

    @staticmethod
    def integer_conversion(dictionary_row):
        for key in dictionary_row:
            dictionary_row[key] = int(dictionary_row[key])
        return dictionary_row

    def return_data_as_integer(self):
        row_values = []
        for row in self.text_data:
            row_values.append(self.integer_conversion(row))
        return row_values



