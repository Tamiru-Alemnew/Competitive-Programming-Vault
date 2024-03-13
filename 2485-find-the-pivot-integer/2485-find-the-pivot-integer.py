class Solution:
    def pivotInteger(self, n: int) -> int:
        ps = [0] * (n +1)
        
        for i in range(1 , n+1):
            ps[i] += i + ps[i-1]

        cur = 0 
        for i in range(n , - 1 , -1):
            cur += i 
            if cur == ps[i] :
                return i 

        return -1 


        