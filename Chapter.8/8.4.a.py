# encoding: utf-8
class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise
        except TypeError:
            if self.muffled:
                print("That wasn't a number, was it?")
            else:
                raise


calculator = MuffledCalculator()
calculator.calc('10/2')
calculator.muffled = True
calculator.calc('10/0')
calculator.calc('10/"a"')
