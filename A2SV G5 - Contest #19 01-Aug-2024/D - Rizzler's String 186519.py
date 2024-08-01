# Problem: D - Rizzler's String - https://codeforces.com/gym/527294/problem/D

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
last_b_ans = 0 

arr = cip()
ans = 0 
for i in range(len(arr)):
    if arr[i] == "a":
        ans += last_b_ans + 1
        ans %=  (10**9 + 7)
    elif arr[i] == "b":
        last_b_ans = ans 

print(ans)