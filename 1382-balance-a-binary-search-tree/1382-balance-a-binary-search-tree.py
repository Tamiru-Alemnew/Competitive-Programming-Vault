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
            md = (l + r )// 2

            cur = TreeNode(elements[md])
            
            if l < md:
                left = build( l , md )

                if  left :
                    cur.left = left

            if md+1 < r:
                right = build( md+1, r )

                if right:
                    cur.right = right
            
            return cur

        root.left = build(0 , md  )
        root.right = build( md+1  , len(elements))

        return root


            


        

        


