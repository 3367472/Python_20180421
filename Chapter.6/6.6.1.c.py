# encoding: utf-8
def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


print(power(2, 10))
