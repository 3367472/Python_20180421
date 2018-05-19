# encoding: utf-8
def func(x):
    return x.isalnum()


seq = ["foo", "x41", "?!", "***"]
print(list(filter(func, seq)))

print([x for x in seq if x.isalnum()])
print(list(filter(lambda x: x.isalnum(), seq)))
