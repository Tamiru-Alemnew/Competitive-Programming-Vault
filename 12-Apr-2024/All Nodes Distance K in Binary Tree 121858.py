# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def map_parents(node, father):
            if node:
                parent[node] = father
                map_parents(node.left, node)
                map_parents(node.right, node)

        map_parents(root , None)

        dist = 0
        queue = deque([target])
        visited = set([target.val])
        ans = []
        while queue and len(ans) == 0 :
            if dist > k :
                break

            for _ in range(len(queue)):
                node = queue.popleft()
                if dist == k :
                    print(dist , node.val)
                    ans.append(node.val)
                    
                if node.right  and node.right.val not in visited:
                    parent[node.right] = node
                    queue.append(node.right)
                    visited.add(node.right.val)

                    
                if node.left and node.left.val not in visited :
                    parent[node.left] = node
                    visited.add(node.left.val)
                    queue.append(node.left)
        
                if node in parent and parent[node] != None :
                    fath = parent[node]
                    if  fath.val not in visited:
                        visited.add(fath.val)
                        queue.append(fath)
            
            dist += 1


        return ans 






                
            



