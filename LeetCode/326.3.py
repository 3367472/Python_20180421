# encoding: utf-8
import math


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            if 3 ** round(math.log(n, 3)) == n:
                return True
        return False


r = Solution()
print(r.isPowerOfThree(27))
print(r.isPowerOfThree(0))
print(r.isPowerOfThree(9))
print(r.isPowerOfThree(45))
print(r.isPowerOfThree(1))
