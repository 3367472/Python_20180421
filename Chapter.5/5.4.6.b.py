# encoding: utf-8
x = [1, 2, 3]
y = [2, 4]
print x is not y
del x[2]
y[1] = 1
print x
print y
y.reverse()
print y
print x == y
print x is y
