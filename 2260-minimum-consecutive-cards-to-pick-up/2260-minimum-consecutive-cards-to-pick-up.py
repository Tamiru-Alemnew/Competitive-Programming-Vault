class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_ind = {}
        ans = float("inf")
        for r  in range(len(cards)):
            if cards[r] in last_ind:
                ans = min(ans ,r- last_ind[cards[r]]+1)

            last_ind[cards[r]] = r

        return -1 if ans == float("inf") else ans 

        