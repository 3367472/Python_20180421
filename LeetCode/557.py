# encoding: utf-8
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        for i in range(len(s_list)):
            s_list[i] = s_list[i][::-1]
        s = ' '.join(s_list)
        return s


r = Solution()
print(r.reverseWords("Let's take LeetCode contest"))
