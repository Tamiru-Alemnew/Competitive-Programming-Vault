
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #check for power of 0
        if n == 0:
            return 1.0

        # check for power by negative number
        if n < 0:
            x = 1 / x
            n =  - n 
        result = 1.0 
        while n > 0:
            if n % 2 == 1:
                result *= x 
            x *= x 
            n =  n // 2
        return result 





        
