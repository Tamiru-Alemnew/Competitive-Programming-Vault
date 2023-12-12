class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        position = {} 
        for i, num in enumerate(nums):
            position[num] = i 
        for i , j in operations:
            if i in position:
                nums[position[i]] = j
                position[j] = position[i]
        return nums