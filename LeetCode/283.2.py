# encoding: utf-8
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(0)
                counter += 1




r = Solution()
nums = [1]
r.moveZeroes(nums)
print(nums)
nums = [0, 1, 0, 3, 12]
r.moveZeroes(nums)
print(nums)
