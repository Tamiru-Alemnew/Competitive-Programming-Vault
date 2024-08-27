# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

import threading
from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
def main():
    n , e = tip()

    arr = lip()

    graph = defaultdict(list)

    for i ,a in enumerate(arr):
        graph[i].append(i+a)

    visited = [False]*(len(arr) + 2)

    def dfs(node , e):
        if visited[node]:
            return
        if node == e -1:
            return True 
        
        visited[node] = True
        for neighbor in graph[node]:
            if  dfs(neighbor, e):
                return True

    if dfs(0, e):
        print("YES")
    else:
        print("NO")

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()