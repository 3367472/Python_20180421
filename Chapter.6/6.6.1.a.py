# encoding: utf-8
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


print(factorial(10))
