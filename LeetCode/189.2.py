# encoding: utf-8
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums = nums[len(nums) - k % len(nums):] + nums[:len(nums) - k % len(nums)]
        print(nums)


r = Solution()
print(r.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(r.rotate([-1, -100, 3, 99], 2))
