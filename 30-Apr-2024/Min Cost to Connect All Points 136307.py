# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        un = UnionFind(len(points))
        graph  = []
        for i in range(len(points)):
            a , b = points[i]
            for j in range(i + 1 , len(points)):
                c , d = points[j] 
                weight = abs(c - a) + abs(d - b)
                graph.append((weight , i , j))

        graph.sort(key = lambda point : point[0])
        minimum_cost = 0
        for weight , a , b in graph:
            if un.find(a) != un.find(b):
                un.union(a , b)
                minimum_cost += weight

        return minimum_cost