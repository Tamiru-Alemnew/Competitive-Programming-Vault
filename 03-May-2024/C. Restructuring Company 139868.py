# Problem: C. Restructuring Company - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C

class UnionFind:
    def __init__(self , n):
        self.parent = {i:i for i in range(n)}
        self.rank = [0 for _ in range(n)]
    def find(self , node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self , node1 , node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 == parent2:
            return
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1

n , m = map(int , input().split())
un = UnionFind(n + 1)
visited = {i:i+1 for i in range(1 , n + 1)}

for i in range(m):
    a , b , c = map(int , input().split())
 
    if a == 3 :
        if un.find(b) == un.find(c):
            print("YES")

        else:
            print("NO")

    elif a == 2:
        while b < c:
            un.union(b, c)
            nxt = visited[b]
            visited[b] = visited[c]
            b = nxt

    else:
        if un.find(b) != un.find(c):
            un.union( b , c)