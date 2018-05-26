# encoding: utf-8
def flatten(nested):
    result = []
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
                result.append(element)
    except TypeError:
        result.append(nested)
    return result


print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
print(list(flatten(['foo', ['bar', ['baz']]])))
