# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        even = 1
        while q:
            prev = q[0].val
            level =[]
            for i in range(len(q)):
                node = q.popleft()
                if even and node.val % 2 != 1:
                    return False
                elif not even and  node.val %2 != 0:
                    return False

                if i > 0 :
                    if (even and node.val <= prev)  or (not even and node.val >= prev): 
                        return False
            
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                prev = node.val

            even = 1 - even 
                
                    
        return True

                    



        