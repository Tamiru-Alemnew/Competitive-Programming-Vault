class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        right = [0] * (n + 1)
        left = [0] * (n + 1)
        l, r = 0, 0

        for i in range(n):
            l += customers[i] == "N"
            left[i + 1] = l

            r += customers[n - i - 1] == "Y"
            right[n - i - 1] = r

        ans = len(right)
        minPenalty = len(right)

        for i in range(len(right)):
            if minPenalty > right[i] + left[i]:
                minPenalty = right[i] + left[i]
                ans = i

        return ans
