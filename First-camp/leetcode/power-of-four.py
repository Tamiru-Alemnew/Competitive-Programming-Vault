class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 4:
            if n == 1:
                return True
            else:
                return False
        else:
            return self.isPowerOfFour(n/4)

