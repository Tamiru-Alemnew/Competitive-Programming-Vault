# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q  = deque([[root , 1]])
        ans = 1

        while q:
            ans = max(ans ,q[len(q)-1][1] -q[0][1] +1 )
            
            for i in range(len(q)):
                node , prev = q.popleft()
                if node.left:
                    q.append([node.left , 2*prev])

                if node.right:
                    q.append([node.right , 2*prev + 1])

        return ans 

            


