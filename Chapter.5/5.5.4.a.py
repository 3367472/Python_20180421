# encoding: utf-8
name = ['anne', 'beth', 'george', 'damon']
age = [12, 45, 32, 102]
for i in range(len(name)):
    print name[i], 'is', age[i], 'years old'

print zip(name, age)
for name, age in zip(name, age):
    print name, 'is', age, 'years old'

print zip(range(5), range(10000000))
