class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        mx = max(nums)
        freq = 0 
        ans = 0 
        l = 0 

        for i in range(len(nums)):
            freq += mx == nums[i]

            while freq >= k and l <= i :
                ans += len(nums) - i 
                freq -= mx == nums[l]
                l += 1 

        return ans 




        