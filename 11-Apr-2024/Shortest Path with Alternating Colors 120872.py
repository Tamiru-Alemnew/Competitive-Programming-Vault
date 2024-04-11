# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        graph = [[[], []] for _ in range(n)] 

        for s , e in redEdges :
            graph[s][0].append(e)

        for s , e in blueEdges:
            graph[s][1].append(e)

        queue = deque([(0 , 0) , (0 , 1)])
        visited = set([(0 , 0) , (0 , 1)])
        answer = [-1 for i in range(n)]
        distance = 0 

        while queue:
            for _ in range(len(queue)):
                node , color = queue.popleft()

                if answer[node] == -1 :
                    answer[node] = distance

                changed_color = 1 - color

                for neighboure in graph[node][changed_color]:
                    if (neighboure , changed_color) not in visited:
                        visited.add((neighboure , changed_color))
                        queue.append((neighboure  , changed_color))
         

            distance += 1

        return answer



