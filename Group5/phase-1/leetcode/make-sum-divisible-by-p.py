class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        remainder = sum(nums) % p
        if remainder == 0:
            return 0

        mod_indices = {0: -1}
        current_mod = 0
        min_length = len(nums)

        for index, num in enumerate(nums):
            current_mod = (current_mod + num) % p
            target_mod = (current_mod - remainder + p) % p
            

            if target_mod in mod_indices:
                min_length = min(min_length, index - mod_indices[target_mod])
      
            mod_indices[current_mod] = index
    
        return -1 if min_length == len(nums) else min_length