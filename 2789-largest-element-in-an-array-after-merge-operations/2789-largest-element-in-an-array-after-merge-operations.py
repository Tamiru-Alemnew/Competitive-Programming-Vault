class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        
        for i in range(len(nums)-2 , -1,-1):
            if nums[i] <= nums[i+1]:
                nums[i] = nums[i] + nums[i+1] 
                nums[i+1] = 0 
                
        return nums[0]


        



        

        