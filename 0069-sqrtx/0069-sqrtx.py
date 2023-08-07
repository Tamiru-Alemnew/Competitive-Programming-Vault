class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
             return x
        
        s , e = 0 , x
        
        while s<e:
            mid = s + (e-s)//2
            if mid*mid == x:
                return mid 
            elif mid*mid > x:
                e = mid
            else: 
                s = mid +1
        return s-1