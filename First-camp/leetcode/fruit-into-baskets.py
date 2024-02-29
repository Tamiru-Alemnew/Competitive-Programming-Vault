class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        l = 0 
        ans =  0 
        cur = 0 
        for r in range(len(fruits)):
            if freq[fruits[r]] == 0 :
                cur += 1 
            freq[fruits[r]] += 1

            while cur > 2 and l < r: 
                freq[fruits[l]] -= 1 
                if freq[fruits[l]] == 0 :
                    cur -= 1   
                l += 1

            ans = max(ans , r - l + 1)

        return ans 

            
            

        