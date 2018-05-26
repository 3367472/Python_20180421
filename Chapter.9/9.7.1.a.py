# encoding: utf-8
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            print(element)


nested = [[1, 2], [3, 4], [5]]

flatten(nested)
