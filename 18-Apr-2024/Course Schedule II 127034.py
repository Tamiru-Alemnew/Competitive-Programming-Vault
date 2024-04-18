# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        incoming = [0]*(numCourses)

        for neighboure  , pre in prerequisites:
            graph[pre].append(neighboure)
            incoming[neighboure] += 1

        answer = []
        queue = deque()

        for i , n in enumerate(incoming) :
            if n == 0 :
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            answer.append(node)
            for nbr in graph[node]:
                incoming[nbr] -= 1

                if incoming[nbr] == 0:
                    queue.append(nbr)
                    

       

        if numCourses != len(answer):
            return []

        return answer

        
        



        



    








        