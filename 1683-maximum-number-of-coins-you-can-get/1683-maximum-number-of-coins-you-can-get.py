class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        coin = 0
        l , r = 1 , len(piles)-1

        while l < r :
            coin += piles[l]
            l += 2
            r -= 1
        return coin 