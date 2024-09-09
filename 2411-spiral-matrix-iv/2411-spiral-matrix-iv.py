# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        grid = [[-1]*n for i in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(r , c):
            return 0<= r < m and 0 <= c < n and grid[r][c] == -1

        cur = 0 

        def dfs(r , c , current):
            nonlocal cur

            if not current:
                return 

            grid[r][c] = current.val

            dr , dc =  directions[cur]
            nr , nc =  r + dr  , c + dc 

            if not inbound(nr , nc):
                cur = (cur + 1)%4 
                dr , dc =  directions[cur]
                nr , nc =  r + dr  , c + dc 

            dfs(nr , nc , current.next)
                
        dfs(0 , 0 , head)

        return grid
            