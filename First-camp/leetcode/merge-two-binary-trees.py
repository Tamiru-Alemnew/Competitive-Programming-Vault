# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def make(root1 , root2 ):
            if not root1 and not root2:
                return 

            elif root1 and not root2:
                return root1
            elif not root1 and root2:
                return root2 

            node = TreeNode(root1.val + root2.val)
            node.left =make(root1.left , root2.left)
            node.right = make(root1.right , root2.right)

            return node

        
        return make(root1 , root2 )
        
            



        
            

        


        