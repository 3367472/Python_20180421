# encoding: utf-8
class MemberCounter():
    members = 0

    def init(self):
        MemberCounter.members += 1


m1 = MemberCounter()
print(m1.members)
m1.init()
print(MemberCounter.members)
print(m1.members)
m2 = MemberCounter()
print(m1.members)
print(m2.members)
m2.init()
print(MemberCounter.members)
print(m1.members)
print(m2.members)
m1.members='Two'
print(MemberCounter.members)
print(m1.members)
print(m2.members)
