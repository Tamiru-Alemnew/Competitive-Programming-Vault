# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree , ans  = [0]*n , []
        for a , b in edges: indegree[b] += 1
        for i in range(n):
            if indegree[i] == 0 : ans.append(i)

        return ans 