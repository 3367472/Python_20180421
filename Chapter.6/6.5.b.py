# encoding: utf-8
def foo():
    x = 42


x = 1
foo()
print(x)


def output(x):
    print(x)


x = 1
y = 2
output(y)


def combine(parameter):
    print(parameter + external)


external = 'berry'
combine('Shrub')
