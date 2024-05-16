# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        
        def bt(l, r ):
            
            if (l, r) in memo:
                return memo[(l, r)]

            if l  > r : return 0
            
            if (r - l +1 ) % 2 == 0 :

                memo[(l , r)] = max( piles[l] + bt( l + 1 , r  ) , piles[r] + bt( l  , r - 1))

            else:
                memo[(l , r)] = min( -piles[l] + bt( l + 1 , r ) , -piles[r] + bt( l  , r - 1 ))

            return memo[(l , r)]

        return bt(0 , len(piles) - 1 ) >  0
    