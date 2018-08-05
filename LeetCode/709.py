# encoding: utf-8
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        str2 = ''
        for x in str:
            str2 = str2 + x.lower()
        return str2

r = Solution()
print(r.toLowerCase("Hello"))
print(r.toLowerCase("here"))
print(r.toLowerCase("LOVELY"))
