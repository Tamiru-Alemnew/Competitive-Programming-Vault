# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

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
    def removeStones(self, stones: List[List[int]]) -> int:
        un = UnionFind(len(stones))
        mp = {}
        for i , (a ,b) in enumerate(stones):
            mp[(a , b)] = i

        sorted_row = sorted(stones , key = lambda point: point[0])
        sorted_col =  sorted(stones , key = lambda point: point[1])
        number_of_stones = 0
        
        for i in range( 1, len(stones)):
            a , b = sorted_row[i]
            c , d = sorted_row[i - 1]

            if a == c :
                if un.find(mp[(a , b)]) != un.find(mp[(c , d)]):
                    un.union(mp[(a , b)], mp[(c , d)])
                    number_of_stones += 1

        for i in range( 1, len(stones)):
            a , b = sorted_col[i]
            c , d = sorted_col[i - 1]

            if b == d :
                if un.find(mp[(a , b)]) != un.find(mp[(c , d)]):
                    un.union(mp[(a , b)], mp[(c , d)])
                    number_of_stones += 1


        return number_of_stones



        