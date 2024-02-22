# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = float("inf")
        prev = float("-inf")

        def Traverse(root):
            if not root:
                return

            nonlocal ans, prev
            Traverse(root.left)
            ans = min(ans, root.val - prev)
            prev = root.val
            Traverse(root.right)

        Traverse(root)
        return ans
            


        


        