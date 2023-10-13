class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        l , r = 0 , len(plants) - 1
        fill = 0
        A = capacityA
        B = capacityB
        while l < r :
            if plants[l] > capacityA:
                fill += 1
                capacityA = A
            capacityA -= plants[l]
            
            if plants[r] > capacityB :
                fill += 1
                capacityB = B
            capacityB -= plants[r]
            l , r = l + 1 , r - 1

            if l == r and max(capacityA , capacityB) < plants[l]: fill += 1
               
        return fill 
