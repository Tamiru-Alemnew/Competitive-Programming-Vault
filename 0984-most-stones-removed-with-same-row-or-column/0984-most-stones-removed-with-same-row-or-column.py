class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        graph = defaultdict(list)
        for i in range(len(stones)):
            for j in range(i+1 , len(stones)):
                ia , ib = stones[i]
                ja , jb = stones[j]

                if ia == ja or ib == jb:
                    graph[(ia , ib)].append((ja , jb))
                    graph[(ja , jb)].append((ia , ib))

        visited = set()
        memo = {}

        def dfs(r , c):
            if (r , c) in visited:
                return 0

            visited.add((r ,c))
            cur = 0
            for nR , nC in graph[(r , c)]:
                cur = max(cur , dfs(nR , nC))

            return cur + 1 

        connected = 0
        for stone in stones:
            if (stone[0] , stone[1])  not in visited:
                connected  +=dfs(stone[0] , stone[1]) - 1

        return connected  


            


        
                