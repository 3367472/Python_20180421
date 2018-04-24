# encoding: utf-8
x = [4, 6, 2, 1, 7, 9]
x.sort()
print x

x = [4, 6, 2, 1, 7, 9]
y = x[:]
y.sort()
print x
print y

x = [4, 6, 2, 1, 7, 9]
y = x
y.sort()
print x
print y

x = [4, 6, 2, 1, 7, 9]
y = sorted(x)
print x
print y

print sorted('Python')
