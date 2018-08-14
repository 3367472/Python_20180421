# encoding: utf-8
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = 0
        str = str.lstrip()
        s_sign = 1
        num_max = 2 ** 31 - 1
        num_min = -2 ** 31
        if len(str) > 0:
            index = 0
            if str[index] == '+':
                index += 1
            elif str[index] == '-':
                s_sign = -1
                index += 1
            while index < len(str):
                if str[index].isnumeric():
                    num = num * 10 + int(str[index])
                    if s_sign == 1:
                        if num > num_max:
                            return num_max
                    elif num > num_max + 1:
                        return num_min
                else:
                    break
                index += 1
        return num * s_sign


r = Solution()
print(r.myAtoi('42'))
print(r.myAtoi('   -42'))
print(r.myAtoi('4193 with words'))
print(r.myAtoi('words and 987'))
print(r.myAtoi('-91283472332'))
print(r.myAtoi(''))
print(r.myAtoi('    '))
print(r.myAtoi('+'))
print(r.myAtoi('+-2'))
print(r.myAtoi('1'))
