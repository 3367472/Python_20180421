# encoding: utf-8
print cmp(42, 32)
print cmp(99, 100)
print cmp(10, 10)
numbers = [5, 2, 9, 7]
numbers.sort(cmp)
print numbers

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
print x

x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print x
