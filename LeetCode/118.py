# encoding: utf-8
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            triangle.append(list([1] * (i + 1)))
            for j in range(1,i):
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle


r = Solution()
print(r.generate(5))
