class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)
        res = ["0"]*len(s)

        for i in range(count["1"]-1):
            res[i] = "1" 

        res[-1] = "1"

        return "".join(res)



        
        