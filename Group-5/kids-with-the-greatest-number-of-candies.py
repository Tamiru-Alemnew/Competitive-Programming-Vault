class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        ans = []
        
        for candy in candies:
            ans.append((candy + extraCandies) >= maximum)

        return ans
