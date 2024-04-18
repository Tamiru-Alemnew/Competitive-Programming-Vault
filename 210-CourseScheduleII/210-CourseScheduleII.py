                
        while queue:
            node = queue.popleft()
            answer.append(node)
            for nbr in graph[node]:
                incoming[nbr] -= 1

                if incoming[nbr] == 0:
                    queue.append(nbr)
                    
        if numCourses != len(answer):
            return []

        return answer

        
        



        



    

2
