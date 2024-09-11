def divide(*args):
    a, b = args

    if not (b == 0):
        inf = a / b
    else:
        from math import inf

    return inf


# print(divide(49, 7))
# print(divide(15, 0))