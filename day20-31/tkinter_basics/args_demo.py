def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 4, 6, 4))
