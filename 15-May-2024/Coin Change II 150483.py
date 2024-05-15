# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # dp = [0]*(amount+1)
        # dp[0] = 1
        
        # for x in coins:
        #     for i in range(x,amount + 1):
        #         if i >= x :
        #             dp[i] += dp[i-x]

        # return dp[amount]

        ans = 0 
        memo = {}
        def dp(i , cur_target):
            nonlocal ans 
            if (i , cur_target) in memo:
                return memo[(i , cur_target)]

            if i == len(coins) or cur_target < 0:
                return 0

            if cur_target == 0 :
                return 1

            nxt = 0
            for j in range( i , len(coins)):
               nxt += dp(j , cur_target - coins[j])

            memo[(i , cur_target)] = nxt

            return nxt

        return dp( 0 , amount)