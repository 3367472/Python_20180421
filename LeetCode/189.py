# encoding: utf-8
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())
        # print(nums)


r = Solution()
print(r.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(r.rotate([-1, -100, 3, 99], 2))
