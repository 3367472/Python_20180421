# encoding: utf-8
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is ', self.value)


class TalkingCaluculator(Calculator, Talker):
    pass


tc = TalkingCaluculator()

print(hasattr(tc, 'talk'))
print(hasattr(tc, 'fnord'))

print(callable(getattr(tc, 'talk', None)))
print(callable(getattr(tc, 'fnord', None)))
