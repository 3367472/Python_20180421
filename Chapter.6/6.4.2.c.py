# encoding: utf-8
def change(n):
    n[0] = 'Mr. Gumby'


names = ['Mrs. Entity', 'Mrs. Thing']
change(names[:])

print(names)
