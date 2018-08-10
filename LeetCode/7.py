# encoding: utf-8
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_list = list(str(x))
        x_list.reverse()
        if x_list[-1] == '-':
            x_list.insert(0, x_list.pop())
        x_str = ''.join('%s' % i for i in x_list)
        x_r = int(x_str)
        if x_r < -(2 ** 31) or x_r > 2 ** 31 - 1:
            x_r = 0
        return x_r


r = Solution()
print(r.reverse(123))
print(r.reverse(-123))
print(r.reverse(120))
