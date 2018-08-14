# encoding: utf-8
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ro_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        ro_dict_2 = {'CM': 'DCD', 'CD': 'CCCC', 'XC': 'LXL', 'XL': 'XXXX', 'IX': 'VIV', 'IV': 'IIII'}
        res = 0
        for key, value in ro_dict_2.items():
            s = s.replace(key, value)
        for c in s:
            res = res + ro_dict[c]
        return res


r = Solution()
print(r.romanToInt('III'))
print(r.romanToInt('IV'))
print(r.romanToInt('IX'))
print(r.romanToInt('LVIII'))
print(r.romanToInt('MCMXCIV'))
