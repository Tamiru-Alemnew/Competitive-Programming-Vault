# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0 for i in range(n)]
        
        for a , b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        queue = deque()
        od  = degree[:]

        for idx , n in enumerate(degree):
            if n == 1:
                queue.append(idx)

        ans = []

        while queue:
            ans = []
            for _ in range(len(queue)):
                node = queue.popleft()
                ans.append(node)
                
                for nbr in graph[node]:
                    degree[nbr] -= 1
                    
                    if degree[nbr] == 1:
                        queue.append(nbr)
                        
        return ans 
        