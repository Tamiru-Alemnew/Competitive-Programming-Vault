# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indgree = [0]*n
        for s , e in edges:
            indgree[e] +=1

        ans = -1

        for i in range(n):
            if indgree[i] == 0:
                if ans == -1:
                    ans = i
                else:
                    return -1

        return ans 