# encoding: utf-8
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index_1 = 0
        index_2 = 0
        len_1 = len(haystack)
        len_2 = len(needle)
        if len_2 > 0:
            result = -1
        else:
            result = 0
        while len_1 >= len_2 and index_1 < len_1 and index_2 < len_2:
            if haystack[index_1] != needle[index_2]:
                result = -1
                index_1 = index_1 - index_2 + 1
                index_2 = 0
            else:
                result = index_1 - index_2
                index_1 += 1
                index_2 += 1
        return result


r = Solution()
print(r.strStr('hello', 'll'))
print(r.strStr('aaaaa', 'bba'))
print(r.strStr('', 'a'))
print(r.strStr('a', ''))
print(r.strStr('', ''))
print(r.strStr('aaa', 'aaa'))
print(r.strStr('aaa', 'aaaa'))
print(r.strStr('mississippi', 'issip'))
