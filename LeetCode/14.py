# encoding: utf-8
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        if len(strs) != 0:
            strs.sort(key=lambda i: len(i))
            for i in range(len(strs[0])):
                flag = True
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        flag = False
                        break
                if flag:
                    result = result + strs[0][i]
                else:
                    break
        return result


r = Solution()
print(r.longestCommonPrefix(["flower", "flow", "flight"]))
print(r.longestCommonPrefix([""]))
print(r.longestCommonPrefix(["dog", "racecar", "car"]))
print(r.longestCommonPrefix(["aca","cba"]))
