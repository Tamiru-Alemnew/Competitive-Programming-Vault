# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cur_count = 0 
        best_count = 0 
        cur_node = root
        res = []

        def inorder(root):
            if not root:
                return 

            
            inorder(root.left)
            nonlocal best_count 
            nonlocal cur_count 
            nonlocal cur_node
            nonlocal res

            if  root.val == cur_node.val:
                cur_count += 1 
            else:
                cur_count = 1 
                cur_node = root

            if cur_count > best_count:
                res =[cur_node.val]
                best_count += 1
            elif cur_count == best_count:
                res.append(cur_node.val)

            inorder(root.right)

        inorder(root)

        return res
