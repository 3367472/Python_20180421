# encoding: utf-8
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print numbers

numbers = [1, 2, 3, 5, 6, 7]
numbers[3:3] = ['four']
print numbers
