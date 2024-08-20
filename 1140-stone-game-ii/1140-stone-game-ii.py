class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        ps = [0]*(len(piles) + 1)
        ps[1] = piles[0]

        for i in range(1 , len(piles)):
            ps[i+1] = piles[i] + ps[i]

       
        @cache
        def dp(m , l):
            if l >= len((ps)):
                return 0


            cur = float("-inf")

            for r in range(l , min(l+2*m , len(ps))):
                next  = ps[r] - ps[l - 1] - dp(max(m , r - l + 1) , r + 1)
                cur = max(cur , next)


            return cur 

    
        bob = (ps[-1] - dp(1 , 1)) // 2

        return ps[-1] - bob



        