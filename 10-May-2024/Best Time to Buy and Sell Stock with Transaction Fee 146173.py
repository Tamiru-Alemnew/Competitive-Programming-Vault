# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        free = 0
        hold = -prices[0]

        for i in range(1 , len(prices)):
            temp = hold
            free = max(free , temp + prices[i] - fee)
            hold = max(temp, free -prices[i])

        return max(free, hold)
