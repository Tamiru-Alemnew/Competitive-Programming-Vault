# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def Traverse(root):
            if not root:
                return 0

            ans = max(Traverse(root.left), Traverse(root.right))

            return 1 + ans 
        
        return Traverse(root)

        
        