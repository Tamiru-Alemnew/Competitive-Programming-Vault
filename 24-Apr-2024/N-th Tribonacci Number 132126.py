# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def tri(n):
            if n in memo:
                return memo[n]
            if n == 2 or n == 1:
                return 1
            elif n == 0 :
                return 0

            memo[n] = tri(n-3) + tri(n-2) + tri(n-1)

            return memo[n]

        return tri(n)
            