# encoding: utf-8
from functools import reduce

numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
print(reduce(lambda x, y: x + y, numbers))

result = 0
for x in numbers:
    result += x
print(result)

print(sum(numbers))
