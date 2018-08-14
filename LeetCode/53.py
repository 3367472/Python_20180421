# encoding: utf-8
import time


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        MaxSum = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum > MaxSum:
                MaxSum = sum
            if sum < 0:
                sum = 0
        return MaxSum


start = time.clock()
r = Solution()
print(r.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
end = time.clock()
print("final is in ", '{:.10f}'.format((end - start) * 1000))
