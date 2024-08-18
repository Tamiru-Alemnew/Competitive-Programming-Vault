# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0]*len(prices)
        sell = [0]*len(prices)
        buy[0] = -prices[0]

        for i in range(1 , len(prices)):
            buy[i] =max(- prices[i] , buy[i-1])
            sell[i] = max(buy[i-1] + prices[i] , sell[i-1])

        return max(buy[-1] , sell[-1])