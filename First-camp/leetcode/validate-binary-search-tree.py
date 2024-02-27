# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True
            
            if not (min_val < node.val < max_val):
                return False
            
            return is_bst(node.left, min_val, node.val) and is_bst(node.right, node.val, max_val)
        
        return is_bst(root)