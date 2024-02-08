class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cur , res = 0 , 0 
        ps_count = {0:1}

        for num in nums:
            cur += num 
            if cur - goal in ps_count:
                res += ps_count[cur-goal]
            ps_count[cur] = ps_count.get(cur, 0) + 1

        return res
