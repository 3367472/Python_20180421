# encoding: utf-8
while True:
    try:
        x = int(input('Enter the first numbar: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x/y is', value)
    except Exception as e:
        print(e)
        print('Please try again.')
    else:
        break
