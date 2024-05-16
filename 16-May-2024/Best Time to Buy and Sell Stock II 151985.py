# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        hold = [0]*len(prices)
        free = [0]*len(prices)
        hold[0] = -prices[0]
        
        for i in range(1 , len(prices)):
            hold[i] = max(free[i -1] - prices[i] , hold[i - 1])
            free[i] = max(free[i - 1] , hold[i - 1] + prices[i])


        return max(hold[-1] , free[-1])
