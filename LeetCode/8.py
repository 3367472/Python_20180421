# encoding: utf-8
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        s_sign = ''
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            s_sign = str[0]
            str = str[1:]
        if str == '' or not str[0].isnumeric() :
            return 0
        else:
            s_num = ''
            for c in str:
                if c == '+':
                    continue
                elif c == '-':
                    s_sign = c
                elif c.isnumeric():
                    s_num = s_num + c
                else:
                    break
            if len(s_num) == 0:
                return 0
            else:
                num = 0
                for i in range(len(s_num)):
                    num = num + int(s_num[-i - 1]) * 10 ** i
                num_max = 2 ** 31 - 1
                num_min = -2 ** 31
                if s_sign == '-':
                    if num > num_max + 1:
                        return num_min
                    else:
                        num = num * -1
                elif num > num_max:
                    return num_max
            return num


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
