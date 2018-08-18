# encoding: utf-8
# 会超时
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


r = Solution()
print(r.pivotIndex([1, 7, 3, 6, 5, 6]))
print(r.pivotIndex([1, 2, 3]))
print(r.pivotIndex([]))
print(r.pivotIndex([-1, -1, -1, -1, -1, -1]))
print(r.pivotIndex([-1, -1, -1, -1, -1, 0]))
print(r.pivotIndex([-1, -1, -1, 0, 1, 1]))
