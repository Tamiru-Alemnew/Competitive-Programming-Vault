# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)
        
        for pre , course in prerequisites:
            graph[pre].append(course)

        grid = [[-1]*numCourses for _ in range(numCourses)]
        visited = set()
        
        def dfs(current):
            if current in visited:
                return 
            visited.add(current)

            for nbr in graph[current]:
                grid[current][nbr] = 1
                dfs(nbr)
                for i in range(numCourses):
                    if grid[nbr][i] == 1:
                        grid[current][i] = 1

        for i in range(numCourses):
            dfs(i)

        res = [False for _ in range(len(queries))]

        for idx, (a , b )in enumerate(queries):
            print
            if grid[a][b] == 1:
                res[idx] = True


        return res



        