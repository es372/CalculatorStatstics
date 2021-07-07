from Calculator.division import division
from Calculator.subtraction import subtraction
from Calculator.squaring import squaring

def variance(list_of_data):
    total = sum(list_of_data)
    sample_size = len(list_of_data)
    squared = []
    for number in list_of_data:
        squared.append(squaring(number))

    squaredTotal = sum(squared)

    numerator = subtraction(squaredTotal, division(squaring(total), sample_size))
    denominator = subtraction(sample_size, 1)

    return division(numerator, denominator)



