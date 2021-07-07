def mode(list_of_data):
    frequency = {}
    highest = 0
    tracking = {}
    for number in list_of_data:
        if number not in frequency:
            frequency[number] = 1

        elif number in frequency:
            frequency[number] += 1

    for value in frequency:
        if frequency[value] > highest:
            highest = frequency[value]
            tracking['mode'] = value

        else:
            pass

    if highest == 1:
        raise Exception('Numbers in dataset have same frequency.')

    return tracking['mode']



