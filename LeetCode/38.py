# encoding: utf-8
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''
        else:
            result = '1'
            for i in range(1, n):
                r_str = ''
                r_num = ''
                r_count = 0
                for c in result:
                    if r_num == '':
                        r_num = c
                        r_count += 1
                    elif r_num == c:
                        r_count += 1
                    else:
                        r_str = r_str + str(r_count) + r_num
                        r_count = 1
                        r_num = c
                r_str = r_str + str(r_count) + r_num
                result = r_str
            return result


r = Solution()
print(r.countAndSay(1))
print(r.countAndSay(2))
print(r.countAndSay(3))
print(r.countAndSay(4))
print(r.countAndSay(5))
print(r.countAndSay(6))
print(r.countAndSay(7))
