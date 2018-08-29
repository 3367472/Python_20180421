# encoding: utf-8
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        return ' '.join(i[::-1] for i in s_list)


r = Solution()
print(r.reverseWords("Let's take LeetCode contest"))
