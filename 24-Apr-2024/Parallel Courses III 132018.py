# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], t: List[int]) -> int:
        if n == 1:
            return t[0]
            
        graph = defaultdict(list)
        incomming = [0 for i in range(n + 1)]
        incomming[0] = 10

        for prev , nxt in relations:
            graph[prev].append(nxt)
            incomming[nxt] += 1

        queue = deque()
        for i in range(1,n+1):
            if incomming[i] == 0:
                queue.append((i , t[i-1]))

        time = 0 
        mp = defaultdict(int)
        ans = 0 
        
        while queue:
            print(queue)
            for _ in range(len(queue)):
                node , tm  = queue.popleft()

                for nbr in graph[node]:
                    incomming[nbr] -= 1

                    if incomming[nbr] == 0:
                        queue.append((nbr , max(tm + t[nbr - 1] , mp[nbr])))
                    else:
                        mp[nbr] = max(mp[nbr], tm + t[nbr - 1])

                ans = max(tm , ans )

        return ans 