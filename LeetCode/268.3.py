# encoding: utf-8
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return list(set(range(len(nums) + 1))-set(nums))[0]


r = Solution()
print(r.missingNumber([3, 0, 1]))
print(r.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(r.missingNumber([0]))
print(r.missingNumber([0, 1]))
