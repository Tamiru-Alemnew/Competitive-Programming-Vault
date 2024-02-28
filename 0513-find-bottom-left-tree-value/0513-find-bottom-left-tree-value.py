# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        prev = 0 
        def helper(root , c):
            nonlocal ans , prev
            if not root:
                return 

            if c > prev:
                ans = root.val
                prev = c

            helper(root.left , c + 1)
            helper(root.right , c + 1)
            
        helper(root , 0)

        return ans 



        
        