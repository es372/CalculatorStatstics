import random

def without_seed(a, b):
    value = round(random.uniform(a, b), 1)
    if value % 1 == 0:
        return int(value)
    else:
        return value



