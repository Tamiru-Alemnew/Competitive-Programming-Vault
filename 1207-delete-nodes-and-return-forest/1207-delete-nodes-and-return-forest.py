# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        queue = deque()
        queue.append(root)
        roots = []
        to_delete = set(to_delete)

        if root.val not in to_delete:
            roots.append(root)

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                if node.val in to_delete and node.left.val not in to_delete:
                    roots.append(node.left)
                if node.left.val  in to_delete:
                    node.left = None
                    
            if node.right:
                queue.append(node.right)
                if node.val in to_delete and node.right.val not in to_delete:
                    roots.append(node.right)

                if node.right.val  in to_delete:
                    node.right = None

        return roots
