# encoding: utf-8
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_1 = len(haystack)
        len_2 = len(needle)
        result = -1
        if len_2 == 0:
            result = 0
        else:
            for i in range(len_1 - len_2 + 1):
                index_1 = i
                index_2 = 0
                while index_1 < len_1 and index_2 < len_2:
                    if haystack[index_1] != needle[index_2]:
                        result = -1
                        index_1 = len_1
                        index_2 = 0
                    else:
                        result = i
                        index_1 += 1
                        index_2 += 1
                if index_2 == len_2:
                    break
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
