# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        for s , e in edges:
            graph[e].append(s)

            
        ancestor = [set([-1]) for i in range(n)]

        def dfs(current):
            if ancestor[current] != set([-1]):
                return 

            ancestor[current] = set()

            for nbr in graph[current]:
                ancestor[current].add(nbr)
                dfs(nbr)

                ancestor[current].update(ancestor[nbr])


        for i in range(n):
            dfs(i)

        for index , ancestorr in enumerate(ancestor):
            cur = list(ancestorr)
            ancestor[index] = sorted(cur)
           
        return ancestor



        