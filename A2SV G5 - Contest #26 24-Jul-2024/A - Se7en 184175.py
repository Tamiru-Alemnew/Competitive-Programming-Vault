# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
    n = ip()
    if n % 7 == 0 :
        print(n)
    else:
        
        temp = n % 7 
        first = n - temp
        second = n + 7 - temp 
        ch1 = first // 10
        ch2 = second // 10
        nch = n // 10
        if ch1 % 10 == nch % 10:
            print(first)
        else:
            print(second)


        