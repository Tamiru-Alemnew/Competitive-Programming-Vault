# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def backtrack(i , current_target):
            
            if i == len(nums):
                if current_target == 0:
                    return 1

                return 0
                
            if (i , current_target) in memo :
                return memo[(i , current_target)]

            possible = 0 
            possible += backtrack(i+1 , current_target + nums[i])
            possible += backtrack(i+1 , current_target - nums[i])

            memo[(i , current_target)] = possible

            return possible

        ans = backtrack(0 , target)

        return ans