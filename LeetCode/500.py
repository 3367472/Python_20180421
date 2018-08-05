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
            for x in range(3):
                if len(line[x]) == len(set(line[x] + i.lower())):
                    result.append(i)
                    break
        return result


r = Solution()
print(r.findWords(["Hello", "Alaska", "Dad", "Peace"]))
