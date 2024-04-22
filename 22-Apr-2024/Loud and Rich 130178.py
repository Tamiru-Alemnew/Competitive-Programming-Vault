# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = defaultdict(list)
        incomming = [0 for _ in range(len(richer))]
        for a , b in richer:
            graph[b].append(a)
            
        res = [-1 for _ in range(len(quiet))]

        def dfs(current):
            if res[current] != -1:
                return

            res[current] = current
            for nbr in graph[current]:
                dfs(nbr)
                if quiet[res[nbr]] < quiet[res[current]]:
                    res[current] = res[nbr]
                    
        for i in range(len(quiet)):
            dfs(i)


        return res



        

        
