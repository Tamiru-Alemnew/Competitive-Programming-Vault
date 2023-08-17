class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.helper(target,nums, 0)
        right = self.helper(target,nums,1)
        return [left,right]

    def helper(self, target,nums, n):
        l , r = 0 , len(nums) - 1
        indx = -1
        while l <= r:
            mid = l +( r - l )//2

            if nums[mid] > target:
                r = mid-1
            elif nums[mid] <target:
                l = mid +1
            else:
                indx = mid
                if n ==0:
                    r =mid-1
                elif n ==1:
                    l = mid +1
        return indx
        



        