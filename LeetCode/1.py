# encoding: utf-8
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        result = []
        for i in range(length):
            num2 = target - nums[i]
            for j in range(i + 1, length):
                if nums[j] == num2:
                    result.append(i)
                    result.append(j)
                    return result


r = Solution()
print(r.twoSum([2, 7, 11, 15], 9))
print(r.twoSum([3, 2, 4], 6))
