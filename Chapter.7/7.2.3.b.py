# encoding: utf-8
class Bird:
    song = 'Squaawk!'

    def sing(self):
        print(self.song)


bird = Bird()
bird.sing()

birdsong = bird.sing
birdsong()
