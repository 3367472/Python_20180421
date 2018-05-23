# encoding: utf-8
class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')

    @classmethod
    def cmech(cls):
        print('This is a class method of ', cls)


MyClass.smeth()
MyClass.cmech()
