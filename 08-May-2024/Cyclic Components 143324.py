# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

import sys
 
N = 200 * 1000 + 11
 
n, m = map(int, input().split())
deg = [0] * N
used = [False] * N
comp = []
g = [[] for _ in range(N)]
 
def dfs(v):
    stack = [v]
    while stack:
        node = stack.pop()
        if not used[node]:
            used[node] = True
            comp.append(node)
            for to in g[node]:
                if not used[to]:
                    stack.append(to)
 
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)
    deg[x] += 1
    deg[y] += 1
 
ans = 0
for i in range(n):
    if not used[i]:
        comp.clear()
        dfs(i)
        ok = all(deg[v] == 2 for v in comp)
        if ok:
            ans += 1
 
print(ans)