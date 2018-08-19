# encoding: utf-8
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])


r = Solution()
print(r.arrayPairSum([1, 4, 3, 2]))
