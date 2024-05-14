# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        memo = {}

        def dp(day , i):

            if i == len(days):
                return 0

            if day in memo:
                return memo[day]

            nxt = float("inf")

            if days[i] < day:
                nxt = dp(day , i + 1)
            else:
                nxt = min(dp(days[i] + 1, i) + cost[0], 
                          dp(days[i] + 7, i) + cost[1],
                          dp(days[i] + 30, i) + cost[2] )

            memo[day] = nxt

            return memo[day] 


        return dp(0 , 0)

            
            

