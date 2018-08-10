# encoding: utf-8
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum:
                left += 1
            elif not s[right].isalnum:
                right -= 1
            elif s[left] != s[right]:
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
