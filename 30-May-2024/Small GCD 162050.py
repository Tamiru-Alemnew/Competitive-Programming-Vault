# Problem: Small GCD - https://codeforces.com/contest/1900/problem/D

import sys
import functools

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    count = [0 for i in range(100001)]
    dp = [0 for i in range(100001)]
    for j in range(n):
        num = a[j]
        d = 1
        while d * d <= num:
            if num % d == 0:
                dp[d] += (n - j - 1) * count[d]
                count[d] += 1
                if d * d != num:
                    dp[num // d] += (n - j - 1) * count[num // d]
                    count[num // d] += 1
            d += 1
    ans = 0
    for j in range(100000, 0, -1):
        for k in range(j + j, 100001, j):
            dp[j] -= dp[k]
        ans += dp[j] * j

    print(ans)
