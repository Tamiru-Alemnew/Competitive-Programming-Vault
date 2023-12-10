class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = s[:spaces[0]] + " "

        for j in range(1, len(spaces)):
            res +=  s[spaces[j- 1]:spaces[j]] + " "

        res +=  s[spaces[-1]:]       
        return res
            