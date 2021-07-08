from Statistics.variance import variance
from Calculator.square_root import square_root

def standard_deviation(list_of_data):
    return square_root(variance(list_of_data))