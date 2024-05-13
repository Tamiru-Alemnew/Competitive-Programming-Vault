# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free = [0]*len(prices)
        hold = [0]*len(prices)
        hold[0] = -prices[0]

        for i in range(1 , len(prices)):
            free[i] = max(free[i- 1] ,hold[i-1] + prices[i])
            hold[i] = max(hold[i-1], free[i-2] - prices[i])

        return max(free[-1] , hold[-1])