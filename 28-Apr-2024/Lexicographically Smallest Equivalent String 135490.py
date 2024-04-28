# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self , n):
        self.parent = [i for i in range(26)]

    def find(self , node):
        if isinstance(node, str):
            node = ord(node) - ord("a")
            
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self , node1 , node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 == parent2:
            return
        if parent1 < parent2:
            self.parent[parent2] = parent1
        else:
            self.parent[parent1] = parent2

    def lex(self , node):
        return chr(self.find(node) + ord("a"))


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        un = UnionFind(26)

        for i in range(len(s1)):
            un.union(s1[i] , s2[i])

        answer = []
        for ch in baseStr:
            cur = un.lex(ch)
            answer.append(cur)


        return "".join(answer)

