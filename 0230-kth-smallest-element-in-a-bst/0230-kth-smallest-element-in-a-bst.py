# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ind = 0
        ans = 0

        def kth(root):
            nonlocal ans  , ind
            if not root:
                return

            res = kth(root.left)
            ind += 1
            if ind == k:
                ans = root.val
                return 

            res2 = kth(root.right)

        kth(root)
        return ans 
        
        