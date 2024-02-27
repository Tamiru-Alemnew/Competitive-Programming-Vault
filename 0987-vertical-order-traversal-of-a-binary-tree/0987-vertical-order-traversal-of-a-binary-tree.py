# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([[root , 0 , 0]])

        while q :
            level = []
            for i in range(len(q)):
                node , r , c  = q.popleft()
                res.append([node.val , r , c])
                if node.left:
                    q.append([node.left , r + 1 , c - 1])
                if node.right:
                    q.append([node.right , r + 1 , c + 1])

        res.sort(key= lambda x : x[2])
        ans=[]
        level = [res[0]]
        
        for i in range(1 , len(res)):
            if level and level[-1][2] == res[i][2]:
                level.append(res[i])

            else:
                level.sort(key = lambda x:x[0])
                level.sort(key = lambda x:x[1])
                tobe = [num[0] for num in level]
                ans.append(tobe)
                level = [res[i]]

        if level:
            level.sort(key = lambda x:x[0])
            level.sort(key = lambda x:x[1])
            ans.append([num[0] for num in level])

        return ans 
        
        





        