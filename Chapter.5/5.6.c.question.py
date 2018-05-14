# encoding: utf-8
boys = ['chris', 'arnold', 'bob']
print boys
girls = ['alice', 'bernice', 'clarice']
print girls
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], [girl])
    print letterGirls
print letterGirls
print [b + '+' + g for b in boys for g in letterGirls[b[0]]]
