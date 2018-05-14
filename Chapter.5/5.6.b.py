# encoding: utf-8
boys = ['chris', 'arnold', 'bob']
print boys
girls = ['alice', 'bernice', 'clarice']
print girls
print [b + '+' + g for b in boys for g in girls if b[0] == g[0]]
