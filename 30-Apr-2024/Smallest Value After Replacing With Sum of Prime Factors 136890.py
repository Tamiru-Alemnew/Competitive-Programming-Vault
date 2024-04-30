# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        
        def prime_factors(n):
            factors = 0 

            while n % 2 == 0:
                factors += 2
                n //= 2

            for i in range(3, int(n**0.5) + 1, 2):
                while n % i == 0:
                    factors += i
                    n //= i

            if n > 1:
                factors += n

            return factors


        while n != prime_factors(n):
            n = prime_factors(n)

        return n 


        