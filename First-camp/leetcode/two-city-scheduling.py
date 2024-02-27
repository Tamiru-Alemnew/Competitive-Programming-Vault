class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0 
        city_b = sorted(costs, key = lambda x: x[0] - x[1])

        for i in range(len(costs)):
            if i < len(costs) //2:
                ans += city_b[i][0]
            else:
                ans += city_b[i][1]

        return ans