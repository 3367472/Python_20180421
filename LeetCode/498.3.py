# encoding: utf-8
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if (not matrix) or (not matrix[0]): return []
        r, c = len(matrix), len(matrix[0])
        if r == 1: return matrix[0]

        res = []
        last_r, last_c = r - 1, c - 1
        for i in range(r + last_c):  # the i-th diagonal
            if i & 1 == 0:  # 斜向上
                cur_r = min(i, last_r)
                cur_c = 0
                if cur_r == last_r:
                    cur_c = i - last_r
                while cur_r >= 0 and cur_c < c:  # 斜上行
                    # print(i, cur_r, cur_c)
                    res.append(matrix[cur_r][cur_c])
                    cur_r -= 1
                    cur_c += 1
            else:  # 斜向下
                cur_c = min(i, last_c)
                cur_r = 0
                if cur_c == last_c:
                    cur_r = i - last_c
                while cur_r < r and cur_c >= 0:  # 斜下行
                    # print(i, cur_r, cur_c)
                    res.append(matrix[cur_r][cur_c])
                    cur_r += 1
                    cur_c -= 1
        return res


r = Solution()
print(r.findDiagonalOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
print(r.findDiagonalOrder([]))
