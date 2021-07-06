import random

def with_seed(a, b):
    random.seed(0)
    value = round(random.uniform(a, b), 1)
    if value % 1 == 0:
        return int(value)
    else:
        return value