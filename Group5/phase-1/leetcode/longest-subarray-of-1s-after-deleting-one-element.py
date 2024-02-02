class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l , r = 0 , 0 
        ans = 0 
        count = {}

        while r < len(nums):
            count[nums[r]] = count.get(nums[r] , 0) + 1
            
            while 0 in count and count[0] > 1 :      
                if nums[l]== 0:
                    count[0] -= 1
                l += 1

            ans= max(r - l , ans )
            r += 1
        return ans 
        



        