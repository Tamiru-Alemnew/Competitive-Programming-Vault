# Problem: B - Mapping the Maze - https://codeforces.com/gym/515998/problem/B

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

n , e = tip()

graph = defaultdict(list)
if e == 1 :
    print("bus topology")
    exit()
for i in range(e):
    v , ed = tip()
    graph[v].append(ed)
    graph[ed].append(v)

ring = True
c = 0 
bus = True
for key , val in graph.items():
    if len(val) == e:
        print("star topology")
        break
    if len(val) !=  2:
        ring = False

    if len(val ) == 1 :
        c += 1
    if len(val) > 2 :
        bus = False
else:
    if ring :
        print("ring topology")
    elif c == 2 and bus :
        print("bus topology")
    else:
        print("unknown topology")



