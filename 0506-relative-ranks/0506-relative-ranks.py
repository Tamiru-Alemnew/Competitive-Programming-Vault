class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = sorted(score , reverse = True )
        l = len(score)
        ans = [0] * len(score)
        print(temp)
        for i , s in enumerate(score):
            if s == temp[0]:
                ans[i] = "Gold Medal"
            elif s == temp[1]:
                ans[i] = "Silver Medal"
            elif  s == temp[2]:
                ans[i] = "Bronze Medal"
            else:
                y = temp.index(s) + 1
                ans[i] = f"{y}"
        return ans
                

        
        