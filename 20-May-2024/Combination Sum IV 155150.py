# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(idx,  cur_target):
            if cur_target in memo :
                return memo[cur_target ]

            if cur_target < 0:
                return 0
            
            if cur_target == 0:
                return 1

            nxt = 0 
            for i in range( len(nums)):
                nxt += dp(i, cur_target - nums[i])

            memo[cur_target]  = nxt

            return memo[cur_target]

        
        return dp(0, target)