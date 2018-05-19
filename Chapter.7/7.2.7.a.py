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
tc.calculate('1+2*3')
tc.talk()

print(TalkingCaluculator.__bases__)
