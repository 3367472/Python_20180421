# encoding: utf-8
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        row_num = len(matrix)
        vol_num = len(matrix[0])
        total = row_num * vol_num
        i = 0
        j = 0
        direct = 1  # 1=up;-1=down
        for x in range(total):
            result.append(matrix[i][j])
            if direct == 1 and i == 0 and j < vol_num - 1:  # 向上，最上侧，右侧还有空间
                direct = -1
                j += 1
            elif direct == 1 and i == 0 and j == vol_num - 1:  # 向上，最上侧，右侧没有空间
                direct = -1
                i += 1
            elif direct == 1 and i > 0 and j == vol_num - 1:  # 向上，最右侧，右侧没有空间
                direct = -1
                i += 1
            elif direct == 1:
                i -= 1
                j += 1
            elif direct == -1 and i < row_num - 1 and j == 0:  # 向下，最左侧，下侧还有空间
                direct = 1
                i += 1
            elif direct == -1 and i == row_num - 1 and j == 0:  # 向上，最左侧，下侧没有空间
                direct = 1
                j += 1
            elif direct == -1 and i == row_num - 1 and j > 0:  # 向上，最下侧，下侧没有空间
                direct = 1
                j += 1
            elif direct == -1:
                i += 1
                j -= 1
        return result


r = Solution()
print(r.findDiagonalOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
