class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate={}
        for i , char in enumerate(nums):
            if char in duplicate:
                return True 
            duplicate[char] = 1 
        return False