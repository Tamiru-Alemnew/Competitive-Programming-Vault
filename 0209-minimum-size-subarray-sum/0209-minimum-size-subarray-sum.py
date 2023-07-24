class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       
        left , right = 0 , 0
        ans = float('inf')
        
        if sum(nums) < target:
            return 0
        s = nums[0]
        while right < len(nums):
            
            if s >= target:
                ans = min(ans, right -left + 1)
                s -= nums[left]
                left += 1
            else:
                right +=1
                if right < len(nums):
                    s += nums[right]
        return ans