class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        # Build the graph
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(s, e, visited):
            if s == e:
                return 1.0

            visited.add(s)

            for neighbor, weight in graph[s]:
                if neighbor not in visited:
                    result = dfs(neighbor, e, visited)
                    if result != -1.0:
                        return result * weight

            visited.remove(s)
            return -1.0

        results = []
        for start, end in queries:
            if start not in graph or end not in graph:
                results.append(-1.0)
            else:
                result = dfs(start, end, set())
                results.append(result)

        return results
