class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 2:
            return n == 1
        else:
            return self.isPowerOfTwo(n / 2)
