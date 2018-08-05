# encoding: utf-8
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        trans_list = []
        for i in range(len(words)):
            trans_str = ""
            for j in words[i]:
                trans_str = trans_str + morse_list[ord(j) - 97]
            trans_list.append(trans_str)
        trans_list = set(trans_list)
        return len(trans_list)


r = Solution()
print(r.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
