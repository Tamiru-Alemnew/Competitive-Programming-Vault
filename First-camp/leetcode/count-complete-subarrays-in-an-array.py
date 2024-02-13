class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_count = len(set(nums))  
        left, right = 0, 0 
        current_count = 0  
        frequency = defaultdict(int)  
        complete_subarrays = 0  

        while right < len(nums):
            if frequency[nums[right]] == 0:
                current_count += 1
            frequency[nums[right]] += 1

            while current_count == total_count:
                complete_subarrays += len(nums) - right  
                frequency[nums[left]] -= 1
                if frequency[nums[left]] == 0:
                    current_count -= 1
                left += 1

            right += 1

        return complete_subarrays
