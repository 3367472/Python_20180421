# encoding: utf-8
x, y, z = 1, 2, 3
print x, y, z

x, y = y, x
print x, y, z

values = 1, 2, 3
print values
x, y, z = values
print x

scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print scoundrel
print key
print value
