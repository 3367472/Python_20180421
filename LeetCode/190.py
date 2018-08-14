# encoding: utf-8
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = bin(n)
        result = result.replace('0b', '', 1)
        result = result.rjust(32, '0')
        return int(result[::-1], 2)


r = Solution()
print(r.reverseBits(43261596))
