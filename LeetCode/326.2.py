# encoding: utf-8
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 1
        while True:
            if n < x:
                return False
            elif n == x:
                return True
            else:
                x *= 3


r = Solution()
print(r.isPowerOfThree(27))
print(r.isPowerOfThree(0))
print(r.isPowerOfThree(9))
print(r.isPowerOfThree(45))
print(r.isPowerOfThree(1))
