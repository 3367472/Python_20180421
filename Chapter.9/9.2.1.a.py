# encoding: utf-8
class A:
    def hello(self):
        print("Hello, I'm A.")


class B(A):
    pass


a = A()
b = B()
a.hello()
b.hello()