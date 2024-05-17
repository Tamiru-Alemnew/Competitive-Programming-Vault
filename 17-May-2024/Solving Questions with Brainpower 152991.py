# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        skip = [0]*n
        do = [0]*n
        for i in range(n - 1 , - 1 , - 1):
            do[i] += questions[i][0]
            if i + questions[i][1] + 1 < n :
                do[i] += max(skip[i + questions[i][1] + 1] , do[i + questions[i][1] + 1])
            if i + 1 < n:  
                skip[i] += max(skip[i + 1] , do[i + 1])

        dd = max(do)
        sk = max(skip)

        return max(dd , sk)