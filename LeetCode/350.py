# encoding: utf-8
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums_inter = list()
        if len(nums1) < len(nums2):
            nums_shorter = nums1
            nums_longer = nums2
        else:
            nums_shorter = nums2
            nums_longer = nums1
        for i in range(len(nums_shorter)):
            if nums_longer.count(nums_shorter[i]) > 0:
                nums_inter.append(nums_shorter[i])
                nums_longer.remove(nums_shorter[i])
        return nums_inter

r = Solution()
print(r.intersect([1, 2, 2, 1],[2, 2, 3]))
