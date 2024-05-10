# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}

        def backtrack(current_target):
            
            min_length = float("inf")

            if current_target in memo:
                return memo[current_target]
            
            if current_target < 0:
                return min_length

            for i in range(len(coins)):
                min_length = min( 1 + backtrack(current_target - coins[i]) , min_length)

            memo[current_target] = min_length

            return min_length

        ans = backtrack(amount)

        return -1 if ans == float("inf") else ans


