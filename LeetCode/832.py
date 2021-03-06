# encoding: utf-8
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i].reverse()
            for j in range(len(A[i])):
                A[i][j] = A[i][j] ^ 1
        return A


r = Solution()
print(r.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(r.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
