class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
    
        prefix_sum = 0
        count = 0
        mod_count = [0] * k
        mod_count[0] = 1

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += mod_count[prefix_sum]
            mod_count[prefix_sum] += 1
            
        return count