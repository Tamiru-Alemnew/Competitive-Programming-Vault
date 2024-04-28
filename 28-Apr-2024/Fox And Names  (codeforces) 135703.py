# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


n = ip()

words = []

for i in range(n):
    words.append(cip())

l = 0 
graph = defaultdict(list)
incomming = defaultdict(int)

for i in range(1, len(words)):
    p = words[i - 1]
    c = words[i]

    d_idx = 0
    while d_idx < len(p) and d_idx < len(c) and p[d_idx] == c[d_idx]:
        d_idx += 1
    
    if d_idx == len(c) and d_idx < len(p):
        print("Impossible")
        exit(0)
    
    if d_idx < len(p) and d_idx < len(c):
        graph[p[d_idx]].append(c[d_idx])
        incomming[c[d_idx]] += 1

queue = deque()

for key , val in graph.items():
    if incomming[key] == 0:
        queue.append(key)


answer = []

while queue :
    node = queue.popleft()
    answer.append(node)
    for nbr in graph[node]:
        incomming[nbr] -= 1
        
        if incomming[nbr] == 0:
            queue.append(nbr)

if len(answer) != len(graph):
    print("Impossible")
else:
    for i in range(26):
        if chr(97 + i) not in answer:
            answer.append(chr(97 + i))
    print("".join(answer))

        