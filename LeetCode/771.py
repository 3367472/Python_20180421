# encoding: utf-8
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for x in J:
                count += S.count(x)
        return count


r = Solution()
print(r.numJewelsInStones("aA", "aAAbbbb"))
print(r.numJewelsInStones("z", "ZZ"))
