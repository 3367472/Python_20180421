# encoding: utf-8
class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm %s." % self.name)


c = Person()
c.setName('Sir Lancelot')
print(c.name)
c.name = 'Sir Gumby'
print(c.getName())
