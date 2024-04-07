# Problem: A - Flag Checker - https://codeforces.com/gym/515998/problem/A

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

x , y = tip()
grid = []
ans = True
for i in range(x):
    temp = input()
    grid.append(temp)
    if  len(set(temp)) > 1:
        ans = False

for i in range(1 , x):
    if grid[i][0] == grid[i-1][0]:
        print("NO")
        break
else:
    if ans :
        print("YES")

    else:
        print("NO")
