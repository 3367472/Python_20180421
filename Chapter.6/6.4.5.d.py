# encoding: utf-8
def foo(x, y, z, m=0, n=0):
    print(x, y, z, m, n)


def call_foo(*args, **kwds):
    print("Calling foo!")
    foo(*args, **kwds)
