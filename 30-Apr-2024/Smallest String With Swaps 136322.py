# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        mp = {}
        for i  , ch in enumerate(s):
            mp[i] = [ch]
            heapify(mp[i])

        un = UnionFind(len(s))

        for p1 , p2 in pairs:
            parent1 = un.find(p1)
            parent2 = un.find(p2)

            if parent1 != parent2:
                un.union(p1 , p2)
                current_pt = un.find(p1)

                if current_pt == parent1 :
                    for w in mp[parent2]:
                        heappush(mp[parent1] , w)

                else:
                    for w in mp[parent1]:
                        heappush(mp[parent2] , w)
        answer = []
        for i in range(len(s)):
            current_word = heappop(mp[un.find(i)])
            answer.append(current_word)

        return "".join(answer)
                

        