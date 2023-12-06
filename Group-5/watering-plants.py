class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0 
        cap = capacity 

        for i , p in enumerate(plants):
            if cap >= p :
                steps += 1
                cap -= p
            else:
                cap = capacity -p 
                steps += 2*i + 1
        return steps
        