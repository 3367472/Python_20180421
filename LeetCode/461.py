# encoding: utf-8
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        xb = bin(x).replace('0b', '')
        yb = bin(y).replace('0b', '')
        if x > y:
            yb = yb.zfill(len(xb))
        elif x < y:
            xb = xb.zfill(len(yb))
        for i in range(len(xb)):
            if xb[i] != yb[i]:
                count += 1
        return count


r = Solution()
print(r.hammingDistance(1, 4))
