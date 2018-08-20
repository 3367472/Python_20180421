# encoding: utf-8
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = -1
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                max_ones = max(max_ones, i - left)
            else:
                left = i
        return max_ones


r = Solution()
print(r.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
