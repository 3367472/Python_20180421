# encoding: utf-8
import shelve

s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']
temp = s['x']
temp.append('d')
s['x'] = temp

print(s['x'])
