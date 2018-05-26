# encoding: utf-8
def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new


r = repeater(42)
print(r.__next__())
print(r.send("Hello world!"))
