class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i , num in enumerate(nums):

            l , r = i + 1 , len(nums) -1
            
            while l < r:
                threesum = num + nums[l] + nums[r]
                if abs(threesum - target) < abs(ans - target):
                    ans = threesum
                if threesum > target: r -=1
                else: l += 1
                    
        return ans