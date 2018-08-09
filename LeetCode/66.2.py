# encoding: utf-8
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(-1, -len(digits) - 1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits


r = Solution()
print(r.plusOne([9]))
print(r.plusOne([1, 2, 3]))
print(r.plusOne([4, 3, 2, 1]))
