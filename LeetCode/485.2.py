# encoding: utf-8
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                max_ones = max(ones, max_ones)
                ones = 0
        return max(ones, max_ones)


r = Solution()
print(r.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
