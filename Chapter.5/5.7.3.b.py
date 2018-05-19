# encoding: utf-8
from math import sqrt

scope = {}
# python2.x
# exec 'sqrt = 1' in scope
# python3.x
exec('sqrt = 1', scope)
print(sqrt(4))
print(scope['sqrt'])
print(len(scope))
print(scope.keys())
print(scope['__builtins__'])
