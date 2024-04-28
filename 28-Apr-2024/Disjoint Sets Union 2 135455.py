# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.min = list(range(1, n + 1))
        self.max = list(range(1, n + 1))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                x_root, y_root = y_root, x_root

            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
            self.min[x_root] = min(self.min[x_root], self.min[y_root])
            self.max[x_root] = max(self.max[x_root], self.max[y_root])

            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def get(self, x):
        x_root = self.find(x)
        return self.min[x_root], self.max[x_root], self.size[x_root]


n, m = map(int, input().split())
uf = UnionFind(n)

for _ in range(m):
    query = input().split()
    if query[0] == 'union':
        uf.union(int(query[1]) - 1, int(query[2]) - 1)
    elif query[0] == 'get':
        min_val, max_val, size = uf.get(int(query[1]) - 1)
        print(f'{min_val} {max_val} {size}')
    
