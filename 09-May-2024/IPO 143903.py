# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cap = []
        pro = []
        for i in range(len(profits)):
            if capital[i] <= w:
                heappush(pro , (-profits[i] , capital[i]))
            else:
                heappush(cap , (capital[i] , - profits[i]))
        ans = 0 

        ow = w
        while k > 0 :
            if pro:
                p , c = heappop(pro)
                w += -p

            while cap and cap[0][0] <= w:
                cp , pr = heappop(cap)
                heappush(pro , (pr , cp))
        
            k -= 1
            
        return w 






