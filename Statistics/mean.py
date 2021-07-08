from Calculator.division import division
from Calculator.addition import addition

def mean(list_of_data):
    sample_size = len(list_of_data)
    total = 0
    for value in list_of_data:
        total = addition(total, value)
    return division(total, sample_size)

