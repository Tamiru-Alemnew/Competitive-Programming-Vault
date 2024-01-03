class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)

        freq = [0] * (max_cost + 1)
        for c in costs:
            freq[c] += 1

        total = 0
        for c in range(1, max_cost+1):
            if freq[c] == 0:
                continue
            if coins <= 0:
                break
            
            if coins > freq[c] * c:
                coins -= freq[c] * c
                total += freq[c]
            else:
                total += coins // c
                break
        return total