import random


def generate_sample(x, a, b):
    data = []
    for i in range(x):
        value = round(random.uniform(a,b), 1)
        if value % 1 == 0:
            randint = int(value)
            data.append(randint)
        else:
            data.append(value)

    return data