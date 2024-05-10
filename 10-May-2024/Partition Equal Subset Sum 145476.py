# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums)
        if half & 1:
            return False

        half //= 2
        memo = set([(0 , nums[0])])

        def backtrack(i , current_sum ):
            nonlocal half

            if current_sum == half:
                return True

            if current_sum > half or i  == len(nums):
                return False

            for j in range(i + 1 , len(nums)):
                current_sum += nums[j]

                if (j , current_sum )in memo:
                    current_sum -= nums[j]
                    continue
                    
                memo.add((j , current_sum))

                if backtrack(j , current_sum):
                    return True

                current_sum -= nums[j]

        return backtrack(0 , nums[0])


