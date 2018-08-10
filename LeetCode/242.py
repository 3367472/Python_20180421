# encoding: utf-8
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = ''.join(set(s))
        if len(s) == len(t):
            for c in letters:
                if s.count(c) != t.count(c):
                    return False
        else:
            return False
        return True


r = Solution()
print(r.isAnagram("anagram", "nagaram"))
print(r.isAnagram("rat", "car"))
