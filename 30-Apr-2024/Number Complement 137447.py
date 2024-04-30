# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        complement , n = 0 , 0

        while num > 0 :
            if num & 1 == 0:
                complement += 2**n

            num >>= 1
            n += 1

        return complement

            



        