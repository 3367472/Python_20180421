# encoding: utf-8
rounds = int(input('How many rounds?'))
sides = 6
sum = 1
if rounds > 1:
    for i in range(2, rounds+1):
        sum += sides * (i - 1)
print('The result is ', sum)
