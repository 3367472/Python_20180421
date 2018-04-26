# encoding: utf-8
x = {}
y = x
x['key'] = 'value'
print y
x.clear()
print y
