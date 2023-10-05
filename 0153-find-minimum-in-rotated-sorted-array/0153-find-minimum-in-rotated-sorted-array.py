class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums) -1 ] or len(nums) == 1:
            return nums[0]
            
        l , r = 0 , len(nums) -1
        while l <= r:
            mid = (l + r) //2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[l]:
                r = mid -1
            else:
                l = mid +1
        
