# encoding: utf-8
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) - 1
        for i in range(m):
            for j in range(i, m - i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[m - j][i]
                matrix[m - j][i] = matrix[m - i][m - j]
                matrix[m - i][m - j] = matrix[j][m - i]
                matrix[j][m - i] = tmp


r = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
r.rotate(matrix)
print(matrix)
matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
r.rotate(matrix)
print(matrix)
