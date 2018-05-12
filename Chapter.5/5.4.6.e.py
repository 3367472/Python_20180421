# encoding: utf-8
number = input('Enter a number between 1 and 10: ')

if number <= 10:
    if number >= 1:
        print 'Great!'
    else:
        print 'Wrong!'
else:
    print 'Wrong!'

if number <= 10 and number >= 1:
    print 'Great!'
else:
    print 'Wrong!'

if 1 <= number <= 10:
    print 'Great!'
else:
    print 'Wrong!'
