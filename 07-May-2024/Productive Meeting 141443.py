# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

from heapq import heapify, heappop, heappush
 
for __ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
 
    heap = []
    for i in range(n):
        if arr[i] > 0:
            heap.append((-1 * arr[i], i + 1))
    
    heapify(heap)
    ans = []
    while len(heap) > 1:
        p1, idx1 = heappop(heap)
        p2, idx2 = heappop(heap)
        p1, p2 = p1 * -1, p2 * -1
 
        ans.append((idx2, idx1))
        p1 -= 1
        p2 -= 1
        if p1 > 0:
            heappush(heap, (p1 * -1, idx1))
        
        if p2 > 0:
            heappush(heap, (p2 * -1, idx2))
    
    print(len(ans))
    for x, y in ans:
        print(x, y)