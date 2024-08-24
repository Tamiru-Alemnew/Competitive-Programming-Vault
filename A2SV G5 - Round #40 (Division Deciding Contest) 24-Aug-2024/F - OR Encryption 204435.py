# Problem: F - OR Encryption - https://codeforces.com/gym/543431/problem/F

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):

    grid = []

    for _ in range(ip()):
        grid.append(lip())
 
    A = [2**30 - 1]*len(grid[0])

    for r in range( len(grid)):
        for c in range( len(grid[0])):
            if r == c :
                continue

            A[c] &= grid[r][c]


    flag = True
    for r in range(len(grid)):
        if not flag:
            break

        for c in range(len(grid[0])):
            if r == c:
                continue
            else:
                if grid[r][c] != (A[c] | A[r]):
                    flag = False
                    break

    if flag:
        print("YES")
        print(*A)
    else:
        print("NO")

