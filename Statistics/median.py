from Calculator.calculator import division
from Calculator.calculator import addition
from Calculator.calculator import subtraction

def median(list_of_data):
    count = len(list_of_data)
    position = division(count, 2)
    if position % 1 == 0:
        integer = int(position)
        numOne = list_of_data[subtraction(integer, 1)]
        numTwo = list_of_data[integer]
        total = addition(numOne, numTwo)
        average = division(total, 2)
        if average % 1 == 0:
             return int(average)

        else:
            return round(average, 2)

    elif position % 1 == 0.5:
        newPos = int(count//2)
        return list_of_data[newPos]
