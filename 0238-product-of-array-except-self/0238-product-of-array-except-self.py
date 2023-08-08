class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        lProduct,rProduct=[1]*n, [1]*n  
        left=right = 1
        
        for i in range(n):
            lProduct[i]= left
            left *= nums[i] 
            
        r = n - 1   
        for i in range(n):
            rProduct[r-i] = right 
            right *=nums[r-i]
            
        for i in range(n):
            output.append(lProduct[i]*rProduct[i])
            
        return output

        