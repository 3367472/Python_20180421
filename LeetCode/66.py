# encoding: utf-8
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits_str = ''.join('%s' % i for i in digits)
            digits_str = str(int(digits_str) + 1)
            digits = list(digits_str)
            digits = list(map(int, digits))
        return digits


r = Solution()
print(r.plusOne([1, 2, 3, 9]))
print(r.plusOne([4, 3, 2, 1]))
