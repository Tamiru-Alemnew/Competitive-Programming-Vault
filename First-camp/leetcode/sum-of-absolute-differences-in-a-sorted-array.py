class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left = 0 
        right = sum(nums) - len(nums)*nums[0]
        ans =[0]*len(nums)
        ans[0] += left + right 
        
        for i in range(1,len(nums)):
            gap = nums[i] - nums[i-1]
            left += gap * i 
            right -= (len(nums) - i ) * gap
            ans[i] += left + right 

        return ans 

        

        