class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        r = len(nums) - 1

        for i in range(len(nums)):
            if nums[i] + nums[0] >= target:
                r = i - 1
                break 

        l = 0 
        ans = 0 
        while r > l :
            if nums[l] + nums[r] < target:
                ans += r -l
                l += 1
            else:
                r -= 1
        return ans 
            


        
        