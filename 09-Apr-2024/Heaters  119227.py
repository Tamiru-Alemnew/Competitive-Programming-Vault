# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        l , r = 0 , int(1e9)
        heaters.sort()
        houses.sort()

        def can_cover(radius):
            num_houses, num_heaters = len(houses), len(heaters)
            house_idx, heater_idx = 0, 0

            while house_idx < num_houses:
                if heater_idx >= num_heaters:
                    return False

                min_range = heaters[heater_idx] - radius
                max_range = heaters[heater_idx] + radius

                if houses[house_idx] < min_range:
                    return False
                if houses[house_idx] > max_range:
                    heater_idx += 1
                else:
                    house_idx += 1

            return True
    
        while l < r : 
            md = (l + r)//2
            if can_cover(md):
                r = md 
            else:
                l = md + 1 

        return l
