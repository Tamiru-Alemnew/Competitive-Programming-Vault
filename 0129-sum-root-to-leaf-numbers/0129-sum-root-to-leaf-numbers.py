# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root , cur):
            nonlocal ans 
            if not root:
                return 

            cur.append(str(root.val))
            if not root.right and not root.left:
                temp = "".join(cur)
                ans += int(temp)

            dfs(root.left , cur)
            dfs(root.right , cur)
            cur.pop()

        dfs(root , [])

        return ans 

            






        