from Calculator.division import division

def mean(list_of_data):
    total = sum(list_of_data)
    sample_size = len(list_of_data)
    return round(division(total, sample_size), 2)

