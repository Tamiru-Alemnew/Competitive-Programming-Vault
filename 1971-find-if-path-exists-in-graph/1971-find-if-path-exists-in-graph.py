class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph =defaultdict(list)
        visited = set()
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(state ):
            if state in visited : return 
            if state == destination:
                return True
            if state not in graph:
                return False

            visited.add(state)
            for s in graph[state]:
                
                if dfs(s):
                    return True

        return dfs(source)
        