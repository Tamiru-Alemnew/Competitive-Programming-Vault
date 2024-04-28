# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()

operations = []
answer = []
for i in range(n):
    oper = input().split()
    operations.append(oper)

min_heap = []
heapify(min_heap)
checker = defaultdict(int)

for i in range(n):
    if operations[i][0] =="insert":
        heappush(min_heap , int(operations[i][1]))
        answer.append(" ".join(operations[i]))
        checker[int(operations[i][1])] += 1
    elif operations[i][0] == "removeMin":
        if min_heap:
            checker[min_heap[0]] -= 1
            heappop(min_heap)
            answer.append(" ".join(operations[ i]))
        else:
            temp = ["insert" , "2"]
            answer.append(" ".join(temp))
            answer.append(" ".join(operations[ i]))
    else:  
        while min_heap and min_heap[0] < int(operations[i][1]):
            checker[min_heap[0]] -= 1
            heappop(min_heap)
            answer.append("removeMin")

        if not min_heap or min_heap[0] != int(operations[i][1]):
            heappush(min_heap , int(operations[i][1]))
            temp = ["insert" , operations[i][1]]
            answer.append(" ".join(temp))
            checker[int(operations[i][1])] += 1

        temp = operations[i]
        answer.append(" ".join(temp))

print(len(answer))
for ans in answer:
    print(ans)





