# encoding: utf-8
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 2:
            cnt = 2
        else:
            cnt = n
        for i in range(2, n):
            j = 2
            while j * j <= i:
                if i % j == 0:
                    cnt += 1
                    break
                j += 1
        return n - cnt


r = Solution()
print(r.countPrimes(10))
print(r.countPrimes(499979))
