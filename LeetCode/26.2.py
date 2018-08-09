# encoding: utf-8
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


r = Solution()
nums_out = [1, 1, 2]
print(nums_out)
print(r.removeDuplicates(nums_out))
print(nums_out)
print(r.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
