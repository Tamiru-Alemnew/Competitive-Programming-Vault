class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        char_index = {}
        ans = 0 
        l = 0
        cur = 0 

        for r in range(len(nums)):
            cur += nums[r]
            if nums[r] in char_index and char_index[nums[r]] >= l:
                cur -=sum(nums[l:char_index[nums[r]] + 1])
                l = char_index[nums[r]] + 1

            char_index[nums[r]] = r
            ans = max(ans , cur)

        return ans 

            

                

        