# encoding: utf-8
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, len(nums1)):
            del nums1[m]
        nums1.extend(nums2[:n])
        nums1.sort()


r = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
r.merge(nums1, m, nums2, n)
print(nums1)
