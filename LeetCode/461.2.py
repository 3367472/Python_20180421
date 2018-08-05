# encoding: utf-8
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')


r = Solution()
print(r.hammingDistance(1, 4))
