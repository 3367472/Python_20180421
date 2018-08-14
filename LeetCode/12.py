# encoding: utf-8
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ro_list = [1000, 500, 100, 50, 10, 5, 1]
        ro_dict = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        ro_dict_2 = {'IIII': 'IV', 'VIV': 'IX', 'XXXX': 'XL', 'LXL': 'XC', 'CCCC': 'CD', 'DCD': 'CM'}
        res = ''
        for c in ro_list:
            cnt = num // c
            num = num % c
            if cnt > 0:
                res = res + ro_dict[c] * cnt
        for key, value in ro_dict_2.items():
            res = res.replace(key, value)
        return res


r = Solution()
print(r.intToRoman(3))
print(r.intToRoman(4))
print(r.intToRoman(9))
print(r.intToRoman(58))
print(r.intToRoman(1994))
