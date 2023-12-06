class Solution:
    def totalMoney(self, n: int) -> int:
        v = 0
        ans = 0 

        for i in range(1 , n + 1):     
            if i % 7 == 1 :
                v = i // 7 + 1
  
            ans +=  v
            v += 1
        return ans 

        