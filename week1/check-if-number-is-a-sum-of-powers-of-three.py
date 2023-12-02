class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        print(1//3)
        while n > 0:
            if n%3 == 2:
                return False
            n //= 3
        return True
        