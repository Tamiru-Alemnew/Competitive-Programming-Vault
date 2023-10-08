class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        temp = sorted(nums)

        if temp[-1] >= 2 * temp[-2]:
            return nums.index(temp[-1]) 
        return -1
        