class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        lP = 1
        for i in range(n):
            res[i] = lP
            lP *= nums[i]
  
        rP = 1  
        for i in range(n-1,-1,-1):
            res[i] *= rP
            rP *= nums[i] 
            
        return res

        