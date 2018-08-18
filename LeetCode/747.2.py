# encoding: utf-8
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxn = max(nums)

        for item in nums:
            if maxn < 2 * item and maxn != item:
                return -1
        return nums.index(maxn)


r = Solution()
print(r.dominantIndex([3, 6, 1, 0]))
print(r.dominantIndex([1, 2, 3, 4]))
print(r.dominantIndex([1]))
