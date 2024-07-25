# Problem: D - A Tree that Needs Addis Hiwot - https://codeforces.com/gym/537362/problem/D

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
    n = int(input())
    parent = list(map(int,input().split()))
    
    graph = [[] for i in range(n)]
    for i in range(n -1):
        graph[parent[i] - 1].append(i + 1)
    
    graph.sort(key = lambda x : len(x),reverse=True)

    arr = []

    for i in graph:
        if len(i) != 0:
            arr.append(len(i))
    
    arr.append(1)

    for i in range(len(arr)):
        arr[i] += i
   
    if max(arr) == arr[-1]:
        print(arr[-1])
        
    else:
        
        cur_ans = arr[-1]
        for i in range(len(arr)):
            arr[i] = -arr[i]
            
        heapify(arr)
        
        while cur_ans < -arr[0]:
            cur = heappop(arr)
            heappush(arr,cur + 1)
            cur_ans += 1
            
        print(cur_ans) 