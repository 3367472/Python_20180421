# encoding: utf-8
strings1 = ['xxx', 'xxxxxxxxx', 'xxxxxxxxx', 'xxxxxxxxx', 'xxxxxxxx']
for string in strings1:
    if 'xxx' in string:
        index = strings1.index(string)  # Search for the string in the list of strings
        strings1[index] = '[censored]'
print strings1

strings2 = ['xxx', 'xxxxxxxxx', 'xxxxxxxxx', 'xxxxxxxxx', 'xxxxxxxx']
index = 0
for string in strings2:
    if 'xxx' in string:
        strings2[index] = '[censored]'
    index += 1
print strings2

strings3 = ['xxx', 'xxxxxxxxx', 'xxxxxxxxx', 'xxxxxxxxx', 'xxxxxxxx']
for index, string in enumerate(strings3):
    if 'xxx' in string:
        strings3[index] = '[censored]'
print strings3
