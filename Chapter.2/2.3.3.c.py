# encoding: utf-8
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print a

a = [1, 2, 3]
b = [4, 5, 6]
print a + b
print a

a = [1, 2, 3]
b = [4, 5, 6]
a = a + b
print a

a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b
print a
