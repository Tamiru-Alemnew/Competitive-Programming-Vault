class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        window = len(cardPoints) - k 
        cur = sum(cardPoints[:window])
        l = 0 
        min_seg = cur

        for r in range(window ,len(cardPoints)):
            cur +=cardPoints[r]
            cur -= cardPoints[l]
            l += 1

            min_seg = min(min_seg , cur )

        return total - min_seg
            









        