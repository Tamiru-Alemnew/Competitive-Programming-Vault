# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self , n):
        self.parent = [i for i in range(n)]
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

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        ans = [False] * len(queries)

        for i in range(len(queries)):
            queries[i].append(i)

        queries.sort(key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])
        j = 0

        for i in range(len(queries)):
            while j < len(edgeList) and edgeList[j][2] < queries[i][2]:
                uf.union(edgeList[j][0], edgeList[j][1])
                j += 1

            ans[queries[i][3]] = (uf.find(queries[i][0]) == uf.find(queries[i][1]))

        return ans
