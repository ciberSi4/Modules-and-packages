def divide(*args):
    a, b = args

    if not (b == 0):
        inf = a / b
    else:
        inf = "Ошибка"

    return inf


# print(divide(69, 3))
# print(divide(3, 0))