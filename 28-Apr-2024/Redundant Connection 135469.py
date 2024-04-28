# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        un = UnionFind(len(edges))
        potential_answers = []

        for a , b in edges:
            a -= 1
            b -= 1
            if un.find(a) == un.find(b):
                potential_answers.append((a , b))

            else:
                un.union(a , b)

        if potential_answers:
            a , b = potential_answers[-1]
            
            return [a + 1 , b + 1]

        return []
            
