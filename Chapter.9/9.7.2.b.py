# encoding: utf-8
def flatten(nested):
    try:
        # 不要迭代类似字符串的对象:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        print(nested)
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
print(list(flatten(['foo', ['bar', ['baz']]])))
