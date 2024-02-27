class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = len(nums) - 1

        for r in range(len(nums) - 2 , -1 ,-1):
            if r + nums[r] >= cur:
                cur = r 
                
        return cur == 0 


        