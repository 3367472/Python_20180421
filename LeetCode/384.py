# encoding: utf-8
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return nums.sort()

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
r = Solution(nums)
print(r.reset())
print(r.shuffle())
