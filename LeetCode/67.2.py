# encoding: utf-8
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a, 2) + int(b, 2), 'b')


r = Solution()
print(r.addBinary('11', '1'))
print(r.addBinary('1010', '1011'))
