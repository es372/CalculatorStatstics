from Calculator.calculator import Calculator
from Statistics.mean import mean
from Statistics.median import median
from Statistics.mode import mode
from Statistics.variance import variance
from Statistics.standard_deviation import standard_deviation

class Statistics(Calculator):

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result




