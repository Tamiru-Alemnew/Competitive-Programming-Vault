# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        elements = []

        def dfs(root):
            if not root :
                return 
            
            dfs(root.left)
            elements.append(root.val)
            dfs(root.right)

        dfs(root)


        md = len(elements) // 2
        root = TreeNode(elements[md])

        def build( l , r):
            if l > r :
                return 
            md = (l + r )// 2

            cur = TreeNode(elements[md])
            
            cur.left = build( l , md-1 )
            cur.right = build( md+1, r )
            
            return cur

        root.left = build(0 , md -1 )
        root.right = build( md+1  , len(elements)-1)

        return root


            


        

        


