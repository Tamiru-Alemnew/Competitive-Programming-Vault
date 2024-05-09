# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = [-i for i in happiness]
        heapify(happiness)
        turn = 0 

        max_happiness = 0 
        while turn < k :
            current_child = heappop(happiness)
            current_happiness = -current_child - turn 
            max_happiness += max(current_happiness , 0 )
            
            turn += 1

        return max_happiness

        