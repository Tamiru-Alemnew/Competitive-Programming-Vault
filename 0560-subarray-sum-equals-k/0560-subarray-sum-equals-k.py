class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur , res = 0 , 0 

        ps_count = {0:1}

        for num in nums:
            cur += num 
            if cur - k in ps_count:
                res += ps_count[cur-k]
            ps_count[cur] = ps_count.get(cur, 0) + 1
        return res