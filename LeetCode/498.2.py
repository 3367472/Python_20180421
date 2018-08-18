# encoding: utf-8
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if len(matrix) > 0:
            row_num = len(matrix) - 1
            vol_num = len(matrix[0]) - 1
            total = (row_num + 1) * (vol_num + 1)
            i = 0
            j = 0
            direct = 1  # 1=up;-1=down
            for x in range(total):
                result.append(matrix[i][j])
                if direct == 1:
                    if j == vol_num:
                        direct = -1
                        i += 1
                    elif i == 0:
                        direct = -1
                        j += 1
                    else:
                        i -= 1
                        j += 1
                else:
                    if i == row_num:
                        direct = 1
                        j += 1
                    elif j == 0:
                        direct = 1
                        i += 1
                    else:
                        i += 1
                        j -= 1
        return result


r = Solution()
print(r.findDiagonalOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
print(r.findDiagonalOrder([]))
