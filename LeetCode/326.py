# encoding: utf-8
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while True:
            if n % 3 == 0:
                n = n / 3
            elif n == 1:
                return True
            else:
                return False


r = Solution()
print(r.isPowerOfThree(27))
print(r.isPowerOfThree(0))
print(r.isPowerOfThree(9))
print(r.isPowerOfThree(45))
