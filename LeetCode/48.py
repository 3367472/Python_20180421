# encoding: utf-8
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        order_num = len(matrix)
        order_half = round(order_num / 2 - 0.1)
        for i in range(order_half):
            for j in range(order_num):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[order_num - i - 1][j]
                matrix[order_num - i - 1][j] = tmp
        for i in range(order_num):
            for j in range(i + 1, order_num):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp


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
