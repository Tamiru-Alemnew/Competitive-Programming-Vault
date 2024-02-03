class Solution:
    def sortSentence(self, s: str) -> str:
        arr = [i[-1] + i[:-1] for i in s.split()]
        
        arr.sort()
        print(arr)
        ans = ""
        for i in arr:
            ans += i[1:] + ' '
        print(ans)
        return ans[:-1]