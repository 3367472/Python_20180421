# encoding: utf-8
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ (2 ** (len(bin(num)) - 2) - 1)


r = Solution()
print(r.findComplement(5))
