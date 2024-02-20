class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        return ((pow(5,n//2+1 , mod))*(pow(4,n//2 , mod)))%mod if n % 2== 1 else ((pow(5 ,n//2,mod ))* (pow(4,n//2 ,mod))) % mod