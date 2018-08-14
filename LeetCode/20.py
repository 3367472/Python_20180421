# encoding: utf-8
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        s_list = []
        s_dict = {')': '(', '}': '{', ']': '['}
        for i in range(len(s)):
            if s[i] in '({[':
                s_list.append(s[i])
            elif s_list == [] or s_dict[s[i]] != s_list.pop():
                return False
        if len(s_list) > 0:
            return False
        return True


r = Solution()
print(r.isValid('()'))
print(r.isValid('()[]{}'))
print(r.isValid('(]'))
print(r.isValid('([)]'))
print(r.isValid('{[]}'))
print(r.isValid(']'))
print(r.isValid('['))
print(r.isValid('(('))
