# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class UnionFind:
    def __init__(self , n):
        self.parent = [i for i in range(0,n + 1)]
        self.rank = [0 for _ in range(n+1)]
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
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        un = UnionFind(n)
        
        for a , b , distance in roads:
            if un.find(a) != un.find(b):
                un.union(a , b)


        min_score = float("inf")

        for a , b , distance in roads:
            if un.find(a) == un.find(1) or un.find(b) == un.find(1):
                min_score = min(min_score , distance)


        return min_score

