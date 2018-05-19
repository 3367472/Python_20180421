# encoding: utf-8
def inc(x):
    x[0] = x[0] + 1


foo = [10]
inc(foo)

print(foo)
