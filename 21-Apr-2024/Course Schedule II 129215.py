# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]

        for course , pre in prerequisites:
            graph[course].append(pre)

        cycle , visited = set() , set()
        answer = []

        def dfs(current , answer):
            if current in cycle :
                return False

            if current in visited:
                return True

            cycle.add(current)
            
            for nbr in graph[current]:
                if not dfs(nbr , answer):
                    return False
                    
            visited.add(current)
            answer.append(current)
            cycle.remove(current)

            return True
        
        for n in range(numCourses):
            if not dfs(n ,answer):
                return []

        return answer
            

            






        
        



        



    








        