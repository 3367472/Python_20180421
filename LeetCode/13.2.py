# encoding: utf-8
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ro_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res = 0
        if len(s) == 1:
            return ro_dict[s]
        else:
            for i in range(1, len(s)):
                if ro_dict[s[i]] > ro_dict[s[i - 1]]:
                    res -= ro_dict[s[i - 1]]
                else:
                    res += ro_dict[s[i - 1]]
            res += ro_dict[s[i]]
            return res


r = Solution()
print(r.romanToInt('III'))
print(r.romanToInt('IV'))
print(r.romanToInt('IX'))
print(r.romanToInt('LVIII'))
print(r.romanToInt('MCMXCIV'))
