# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        que = deque()
        que.append(root)
        res =[]

        while que:
            temp_que = deque()
            temp=[]

            for i in range(len(que)):
                node = que.popleft()
                temp.append(node.val)

                if node.left:
                    temp_que.append(node.left)
                if node.right:
                    temp_que.append(node.right)
            que = temp_que
            res.append(temp)
            
        return res