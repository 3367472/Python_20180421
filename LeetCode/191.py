# encoding: utf-8
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

r = Solution()
print(r.hammingWeight(11))
print(r.hammingWeight(128))
