# encoding: utf-8
print [x * x for x in range(10)]
print [x * x for x in range(10) if x % 3 == 0]
print [(x, y) for x in range(3) for y in range(3)]

result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
print result