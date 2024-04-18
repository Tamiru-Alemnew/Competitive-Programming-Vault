# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outgoing = []
        reversed_graph =[[] for i in range(len(graph))]
        
        for i , neighboure in enumerate(graph):
            for nbr in neighboure:
                reversed_graph[nbr].append(i)

        for neighboure in graph :
            outgoing.append(len(neighboure))

        queue = deque()

        for i ,  n in enumerate(outgoing):
            if n == 0 :
                queue.append(i)

        answer = []

        while queue:
            node = queue.popleft()
            answer.append(node)
            for nbr in reversed_graph[node]:
                outgoing[nbr] -= 1
                
                if outgoing[nbr] == 0:
                    queue.append(nbr)
                

        return sorted(answer)