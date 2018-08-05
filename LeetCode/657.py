# encoding: utf-8
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        coordinate = [0, 0]
        result = False
        for i in moves:
            if i == "U":
                coordinate[1] += 1
            if i == "D":
                coordinate[1] -= 1
            if i == "L":
                coordinate[0] -= 1
            if i == "R":
                coordinate[0] += 1
        if coordinate == [0, 0]:
            result = True
        return result

r = Solution()
print(r.judgeCircle("UD"))
print(r.judgeCircle("LL"))
print(r.judgeCircle("LR"))
print(r.judgeCircle("RDLU"))
