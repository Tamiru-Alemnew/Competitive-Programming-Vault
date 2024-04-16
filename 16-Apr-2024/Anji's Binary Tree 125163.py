# Problem: Anji's Binary Tree - https://codeforces.com/contest/1900/problem/C

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0


for _ in range(ip()):
    n = ip()
    dir =["Tamiru"] + cip()
    tree = [["Alemnew"]]
 
    for i in range(n):
        a , b = tip()
        tree.append([a , b])
    
    ans = inf
    ch = 0
    stack = [(1 , 0)]

    while stack:
        node , ch = stack.pop()
        if tree[node][0] == tree[node][1] == 0:
            ans = min(ch , ans)
            continue
        
        if dir[node] == "U" :
            ch += 1

        if tree[node][0] != 0 :

            ch += dir[node] == "R"
            stack.append((tree[node][0] , ch))
            ch -= dir[node] == "R" 

        if tree[node][1] != 0 :
    
            ch += dir[node] == "L"
            stack.append((tree[node][1] , ch))
            ch -= dir[node] == "L" 

        ch -=  dir[node] == "U"

    print(ans)