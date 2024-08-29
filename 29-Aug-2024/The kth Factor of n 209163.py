# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        lower = []
        upper = []
        r = int(math.sqrt(n))
        
        for i in range(1 , r + 1):
            if n % i ==0 and upper and i == upper[-1] :
                lower.pop()
                upper.pop()

            if n % i ==0:
                lower.append(i)
                upper.append(n//i)

        while upper and len(lower) < k:
            cur = upper.pop()
            if cur != lower[-1]:
                lower.append(cur)

        return -1 if len(lower) < k else lower[k-1]