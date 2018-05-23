# encoding: utf-8
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError


r = Rectangle()
print(r.size)
r.width = 10
print(r.size)
r.height = 5
print(r.size)

r.size = 150, 100
print(r.width)
print(r.size)
