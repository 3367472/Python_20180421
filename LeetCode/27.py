# encoding: utf-8
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[right] == val:
                right -= 1
            elif nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            else:
                left += 1
        return right + 1


r = Solution()
print(r.removeElement([3, 2, 2, 3], 3))
print(r.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(r.removeElement([1], 1))
