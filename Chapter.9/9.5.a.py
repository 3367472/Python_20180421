# encoding: utf-8
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height


r = Rectangle()
print(r.getSize())
r.width = 10
print(r.getSize())
r.height = 5
print(r.getSize())

r.setSize((150, 100))
print(r.width)
print(r.getSize())
