# Problem: G - Small Town - https://codeforces.com/gym/543431/problem/G

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n = ip()

    arr = lip()

    arr.sort()

    def chk(t):
        cnt = 1
        l = arr[0] + t

        for i in range(len(arr)):
            if abs(l - arr[i]) > t:
                cnt += 1
                l =  arr[i] + t

            if cnt > 3 :
                return False
            
        return True
    
    l , r = 0 , 10**9

    while l < r :
        md = (l + r) // 2

        if chk(md):
            r = md 

        else:
            l = md + 1


    print(r)

            



