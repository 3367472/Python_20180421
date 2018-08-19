# encoding: utf-8
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        min_sum = 0
        for i in range(0, len(nums), 2):
            min_sum += nums[i]
        return min_sum


r = Solution()
print(r.arrayPairSum([1, 4, 3, 2]))
