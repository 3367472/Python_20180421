# encoding: utf-8
import shelve

s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']
s['x'].append('d')

print(s['x'])
