# encoding: utf-8
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        nums_inter = list()
        nums1_i = 0
        nums2_i = 0
        while nums1_i < len(nums1) and nums2_i < len(nums2):
            if nums1[nums1_i] == nums2[nums2_i]:
                nums_inter.append(nums1[nums1_i])
                nums1_i += 1
                nums2_i += 1
            elif nums1[nums1_i] > nums2[nums2_i]:
                nums2_i += 1
            else:
                nums1_i += 1
        return nums_inter


r = Solution()
print(r.intersect([1, 2, 2, 1], [2, 2]))
