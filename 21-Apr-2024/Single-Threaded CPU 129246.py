# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        cur_tasks = []
        for i , cur in enumerate(tasks):
            cur.append(i)
            cur_tasks.append(cur)

        cur_tasks.sort(key = lambda x : x[0])
        current_time = cur_tasks[0][0]
        min_heap = [[cur_tasks[0][1] , cur_tasks[0][2]]]
        heapify(min_heap)
        current_idx = 1
        answer = []

        while min_heap or current_idx < len(tasks):

            if not min_heap :
                current_time = max(current_time,cur_tasks[current_idx][0])
                
            while current_idx < len(tasks) and current_time >= cur_tasks[current_idx][0]:
                heappush(min_heap ,[cur_tasks[current_idx][1] , cur_tasks[current_idx][2]])
                current_idx += 1


            time , item = heappop(min_heap)
            answer.append(item)
            current_time  += time
                
                
        return answer


        