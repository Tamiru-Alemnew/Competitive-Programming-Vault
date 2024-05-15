# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dp(target):
            if target in memo:
                return memo[target]

            if target == 1:
                return 1


            max_product = 0
            for i in range(1, target):

                max_product = max(max_product, i * max(target - i, dp(target - i)))
                
            memo[target] = max_product

            return max_product
        
        return dp(n)