# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import defaultdict
x = int(input())

for _ in range(x):
    y = int(input())
    factors = defaultdict(int)
    arr = list(map(int , input().split()))

    for n in arr:
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors[i] +=1
        if n > 1:
            factors[n] +=1

    for key , val in factors.items():
        if val % y:
            print("NO")
            break
    else:
        print("YES")