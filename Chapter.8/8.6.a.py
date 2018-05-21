# encoding: utf-8
class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except (ZeroDivisionError, TypeError, NameError) as e:
            print(e)


calculator = MuffledCalculator()
calculator.calc('10/2')
calculator.muffled = True
calculator.calc('10/0')
calculator.calc('10/"a"')
