# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)
        res = []
        if root and  root.val not in delete:
            res.append(root)
        def deleter(root , delete , res):
            if not root:
                return

            if root.val not in delete:
                root.left = deleter(root.left , delete , res)
                root.right = deleter(root.right , delete ,res)
            else:
                if root.left :
                    res.append(deleter(root.left , delete , res))
                if root.right:
                    res.append(deleter(root.right , delete, res))
                return None

            return root 

        deleter(root , delete , res)

        return [r for r in res if r]