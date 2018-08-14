# encoding: utf-8
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre = 1
        cur = 1
        for i in range(1, n):
            tmp = pre
            pre = cur
            cur = tmp + pre
        return cur



r = Solution()
print(r.climbStairs(2))
print(r.climbStairs(3))
print(r.climbStairs(4))
print(r.climbStairs(5))
