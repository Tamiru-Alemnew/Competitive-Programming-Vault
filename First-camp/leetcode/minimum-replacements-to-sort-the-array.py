class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0 

        for i in range(len(nums)-2 ,-1,-1):
            if nums[i] > nums[i+1]:
                s = math.ceil(nums[i] / nums[i+1])
                p = nums[i] // s
                nums[i] = p
                ans +=  s - 1

        return ans




        