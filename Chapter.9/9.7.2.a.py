# encoding: utf-8
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


nested = [[1, 2], [3, 4], [5]]

for num in flatten(nested):
    print(num)

print(list(flatten(nested)))

print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))