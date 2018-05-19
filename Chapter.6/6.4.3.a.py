# encoding: utf-8
def hello_1(greeting, name):
    print('%s, %s!' % (greeting, name))


def hello_2(name, greeting):
    print('%s, %s!' % (name, greeting))


hello_1('Hello', 'world')
hello_2('Hello', 'world')

hello_1(greeting='Hello', name='world')
hello_1(name='world', greeting='Hello')

hello_2(greeting='Hello', name='world')


def hello_3(greeting='Hello', name='world'):
    print('%s, %s!' % (greeting, name))


hello_3()
hello_3('Greetings')
hello_3('Greetings', 'universe')

hello_3(name='Gumby')
