class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose = {}
        for match in matches:
            lose[match[1]] = lose.get(match[1] , 0) + 1
            if match[0] not in lose:
                lose[match[0]] = 0
        ans = []
        for i in range(2):
            ls = [k for k , v  in lose.items() if v==i ]
            ls.sort()
            ans.append(ls)
            

        return ans