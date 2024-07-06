class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rem = time % (n - 1)
        parity = time //  ( n -1)

        if parity % 2 == 0 :
            if rem == 0 :
                return 1
                
            return rem + 1
        else:
            return n - rem 

