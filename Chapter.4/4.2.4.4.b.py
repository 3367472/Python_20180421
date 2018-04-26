# encoding: utf-8
d = {}
print d.get('name')
print d.get('name', 'N/A')

d['name'] = 'Eric'
print d.get('name')
