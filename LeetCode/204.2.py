# encoding: utf-8
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        else:
            res = [True] * n
            res[0] = False
            res[1] = False
            for i in range(2, int(n ** 0.5) + 1):
                if res[i]:
                    res[i * i:n:i] = [False] * len(res[i * i:n:i])
        return sum(res)


r = Solution()
print(r.countPrimes(10))
print(r.countPrimes(100))
print(r.countPrimes(499979))
