# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        
        def help(root , mx , mn):
            nonlocal ans 
            if not root:
                return 

            mx = max(mx , root.val)
            mn = min(mn , root.val)
            ans = max(ans , abs(mx -mn))
            
            help(root.left , mx , mn)
            help(root.right, mx , mn)

        help(root , root.val ,root.val)

        return ans 



        

        