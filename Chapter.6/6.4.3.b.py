# encoding: utf-8
def hello_4(name, greeting='Hello', punctuation='!'):
    print('%s, %s%s' % (greeting, name, punctuation))


hello_4('Mars')
hello_4('Mars', 'Howdy')
hello_4('Mars', 'Howdy', '...')
hello_4('Mars', punctuation='.')
hello_4('Mars', greeting='Top of the morning to ya')
hello_4()
