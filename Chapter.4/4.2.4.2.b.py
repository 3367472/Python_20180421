# encoding: utf-8
from copy import deepcopy

d = {}
d['name'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['name'].append('Clive')
print c
print dc
