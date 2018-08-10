# encoding: utf-8
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        s_clr = ''
        for c in s:
            if c.isalnum():
                s_clr = s_clr + c
        if len(s_clr) <= 1:
            return True
        else:
            s_clr = s_clr.lower()
            for c in range(round(len(s_clr) / 2)):
                if s_clr[c] != s_clr[-c - 1]:
                    return False
        return True


r = Solution()
print(r.isPalindrome('A man, a plan, a canal: Panama'))
print(r.isPalindrome('race a car'))
print(r.isPalindrome(''))
print(r.isPalindrome(',.'))
print(r.isPalindrome('1a2'))
print(r.isPalindrome('......a.....'))
print(r.isPalindrome('0z;z   ; 0'))
