class Solution:
    def numberOfWays(self, s: str) -> int:
        preZero = [0]*len(s)
        preOne = [0]*len(s)
        sufOne =[0]*len(s)
        sufZero =[0]*len(s)

        for i in range(len(s)):
            if s[i] =="1":
                preOne[i] += 1
                sufOne[i] += 1
            else:
                preZero[i] += 1
                sufZero[i] += 1 

        for  i in range(1,len(s)):
            preOne[i] += preOne[i-1]
            preZero[i] += preZero[i-1]

        for i in range(len(s)-2 , - 1 , -1):
            sufOne[i] += sufOne[i+1]
            sufZero[i] += sufZero[i+1]
        ans = 0

        for i in range(len(s)):
            if s[i] == "1":
                ans += preZero[i] * sufZero[i]

            else:
                ans += preOne[i] * sufOne[i]       
        return ans 