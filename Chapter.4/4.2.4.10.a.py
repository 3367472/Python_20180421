# encoding: utf-8
d = {}
print d.setdefault('name', 'N/A')
print d
d['name'] = 'Gumby'
print d.setdefault('name', 'N/A')
print d

d={}
print d.setdefault('name')
print d