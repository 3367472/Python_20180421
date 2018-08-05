# encoding: utf-8
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


r = Solution()
print(r.reverseString("hello"))
