# encoding: utf-8
def hello_3(greeting, name):
    print('%s, %s!' % (greeting, name))


params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**params)
