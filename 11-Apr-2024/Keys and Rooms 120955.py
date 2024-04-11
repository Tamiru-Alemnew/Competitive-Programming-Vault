# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        ans = [0]*len(rooms)

        queue = deque([0])
        visited = set([0])
        ans[0] = 1

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                ans[node] = 1

                for neighboure in rooms[node]:
                    if neighboure not in visited:
                        queue.append(neighboure)
                        visited.add(neighboure)


        return all(opened == 1 for opened in ans)

