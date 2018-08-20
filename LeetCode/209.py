# encoding: utf-8
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums) + 1
        tmp_sum = 0
        for i in range(len(nums)):
            if nums[i] == s:
                return 1
            elif nums[i] > s:
                continue
            elif nums[i] < s:
                for j in range(len(nums[i:])):
                    tmp_sum += nums[i + j]
                    if tmp_sum > s:
                        tmp_sum = 0
                    elif tmp_sum < s:
                        continue
                    elif tmp_sum == s:
                        result = min(result, j + 1)
        if result == len(nums) + 1:
            return 0
        else:
            return result


r = Solution()
print(r.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(r.minSubArrayLen(11, [1, 2, 3, 4, 5]))
