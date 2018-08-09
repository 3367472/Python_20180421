# encoding: utf-8
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


r = Solution()
print(r.containsDuplicate([1, 2, 3, 1]))
print(r.containsDuplicate([1, 2, 3, 4]))
print(r.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
