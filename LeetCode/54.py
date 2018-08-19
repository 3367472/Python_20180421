# encoding: utf-8
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return matrix
        else:
            result = []
        row_num = len(matrix) - 1
        vol_num = len(matrix[0]) - 1
        total = (row_num + 1) * (vol_num + 1)
        i = 0
        j = 0
        edge = 0
        direct = 1  # 1=right;2=down;3=left;4=up
        for x in range(total):
            result.append(matrix[i][j])
            if direct == 1:
                if j == vol_num - edge:  # 向上，最上侧，右侧还有空间
                    direct = 2
                    i += 1
                else:
                    j += 1
            elif direct == 2:
                if i == row_num - edge:  # 向上，最上侧，右侧没有空间
                    direct = 3
                    j -= 1
                else:
                    i += 1

            elif direct == 3:
                if j == edge:  # 向上，最右侧，右侧没有空间
                    direct = 4
                    i -= 1
                    edge += 1
                else:
                    j -= 1
            elif direct == 4:
                if i == edge:
                    direct = 1
                    j += 1
                else:
                    i -= 1
        return result


r = Solution()
print(r.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
print(r.spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]))
print(r.spiralOrder([]))
