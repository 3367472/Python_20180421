# encoding: utf-8
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stock_sum = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                stock_sum = stock_sum + prices[i + 1] - prices[i]
        return stock_sum


r = Solution()
print(r.maxProfit([7, 1, 5, 3, 6, 4]))
print(r.maxProfit([1, 2, 3, 4, 5]))
print(r.maxProfit([7, 6, 4, 3, 1]))
