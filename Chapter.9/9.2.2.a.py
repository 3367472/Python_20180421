# encoding: utf-8
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No, thanks!')


class Songbird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawek!'

    def sing(self):
        print(self.sound)


b = Bird()
b.eat()
b.eat()

sb = Songbird()
sb.sing()
sb.eat()
sb.eat()

