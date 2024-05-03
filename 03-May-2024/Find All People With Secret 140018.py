# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

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
    def reset(self , u):
        self.parent[u] = u

class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        meeting_ordered = defaultdict(list)
        for x , y , time in meetings:
            meeting_ordered[time].append((x , y))
        un = UnionFind(n)
        un.union(0 , firstPerson)

        for _, pairs in sorted(meeting_ordered.items(), key=lambda x: x[0]):
            check = set()
            for x , y in pairs:
                if un.find(x) != un.find(y):
                    un.union(x , y)
                    check.add(x)
                    check.add(y)

            for u in check:
                if un.find(u) != un.find(0):
                    un.reset(u)

        return [i for i in range(n) if un.find(i) == un.find(0)]

