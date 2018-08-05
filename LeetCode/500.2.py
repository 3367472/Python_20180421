# encoding: utf-8
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        for i in words:
            for j in line:
                flag = True
                for k in i.lower():
                    if j.count(k) == 0:
                        flag = False
                        break
                if flag:
                    result.append(i)
                    break
        return result


r = Solution()
print(r.findWords(["Hello", "Alaska", "Dad", "Peace"]))
