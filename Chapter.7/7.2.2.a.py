# encoding: utf-8
class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm %s." % self.name)


foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()
bar.greet()

print(foo.name)
print(bar.name)

bar.name = 'Yona'
bar.greet()

Person.greet(foo)
Person.greet(bar)
