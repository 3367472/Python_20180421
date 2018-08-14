# encoding: utf-8
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = "{:0>32b}".format(n)
        return int(result[::-1], 2)


r = Solution()
print(r.reverseBits(43261596))
