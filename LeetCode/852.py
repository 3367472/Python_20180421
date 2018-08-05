# encoding: utf-8
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))


r = Solution()
print(r.peakIndexInMountainArray([0, 1, 0]))
print(r.peakIndexInMountainArray([0, 2, 1, 0]))
