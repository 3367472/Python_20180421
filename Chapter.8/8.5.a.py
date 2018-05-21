# encoding: utf-8
class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except (ZeroDivisionError, TypeError, NameError):
            if self.muffled:
                print('Your numbers were bogus...')
            else:
                raise


calculator = MuffledCalculator()
calculator.calc('10/2')
calculator.muffled = True
calculator.calc('10/0')
calculator.calc('10/"a"')
