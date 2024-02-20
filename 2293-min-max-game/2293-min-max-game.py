class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        cur = [0]*(n//2)
        for i in range(n//2):
            if i % 2==0:
                cur[i] = min(nums[2 * i], nums[2 * i + 1])
            else:
                cur[i] = max(nums[2 * i], nums[2 * i + 1])

        return self.minMaxGame(cur)


    




        
         
    