# encoding: utf-8
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        max_num_index = nums.index(max_num)
        nums.pop(max_num_index)
        for i in range(len(nums)):
            if max_num >= (max(nums) << 1):
                return max_num_index
            else:
                return -1
        return max_num_index


r = Solution()
print(r.dominantIndex([3, 6, 1, 0]))
print(r.dominantIndex([1, 2, 3, 4]))
print(r.dominantIndex([1]))
