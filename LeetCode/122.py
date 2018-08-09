# encoding: utf-8
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stock_sum = 0
        stock_in = 0
        stock_status = 0
        for i in range(len(prices) - 1):
            if stock_status == 0 and prices[i] < prices[i + 1]:
                stock_in = prices[i]
                stock_status = 1
            elif stock_status == 1 and prices[i] > prices[i + 1]:
                stock_sum = stock_sum + prices[i] - stock_in
                stock_status = 0
            if stock_status == 1 and i == len(prices) - 2:
                stock_sum = stock_sum + prices[i + 1] - stock_in
                stock_status = 0
        return stock_sum


r = Solution()
print(r.maxProfit([7, 1, 5, 3, 6, 4]))
print(r.maxProfit([1, 2, 3, 4, 5]))
print(r.maxProfit([7, 6, 4, 3, 1]))
