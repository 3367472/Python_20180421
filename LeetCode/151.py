# encoding: utf-8
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(' ')
        s_list = list(filter(None, s_list))
        s_list.reverse()
        s = ' '.join(s_list)
        return s


r = Solution()
print(r.reverseWords("the sky is blue"))
print(r.reverseWords("     the sky is blue     "))
print(r.reverseWords("     the     sky     is     blue     "))
