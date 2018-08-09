# encoding: utf-8
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global nums_out
        nums_out = list(set(nums))
        return len(nums_out)


r = Solution()
nums_out = [1, 1, 2]
print(nums_out)
print(r.removeDuplicates(nums_out))
print(nums_out)
print(r.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
