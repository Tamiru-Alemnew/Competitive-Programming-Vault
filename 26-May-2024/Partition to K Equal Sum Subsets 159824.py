# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target = total_sum // k
        nums.sort(reverse=True)
        n = len(nums)

        @lru_cache(None)
        def dp(mask, current_sum, count):
            if count == k:  
                return True

            if current_sum == target: 
                return dp(mask, 0, count + 1)

            for i in range(n):
                if not (mask & (1 << i)) and current_sum + nums[i] <= target:
                    if dp(mask | (1 << i), current_sum + nums[i], count):
                        return True
                        
            return False

        return dp(0, 0, 0)
