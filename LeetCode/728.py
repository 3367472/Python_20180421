# encoding: utf-8
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right + 1):
            flag = True
            for j in str(i):
                if j == '0' or i % int(j) > 0:
                    flag = False
            if flag:
                result.append(i)
        return result


r = Solution()
print(r.selfDividingNumbers(1, 22))
