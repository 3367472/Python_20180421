# encoding: utf-8
scope = {}
exec('x = 2', scope)
print(eval('x * x', scope))
