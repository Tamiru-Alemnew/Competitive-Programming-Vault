class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for i in range(n)]

        p = 2

        while p * p <= n-1 :
            if prime[p]:
                for i in range(p*p , n  , p):
                    prime[i]= False

            p += 1

        ans = 0 
        for i in range(2 , n ):
            ans += prime[i] == True

        return ans 

        

        