class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        stack = [0]

        for i in range(1 , len(nums)):
            if stack and nums[stack[-1] ] > nums[i]:
                stack.append(i)
        l = len(nums)
        ans = 0 
        for i in range(len(nums) - 1 , -1 , -1):
            while stack and nums[stack[-1]] <= nums[i]:
                l = stack.pop()
            ans = max(i - l ,  ans)

        return ans 

        
