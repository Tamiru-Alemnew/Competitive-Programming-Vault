class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        ans = k
        for i in range(k):
            count[nums[i]] += 1

        l = 0 
        for i in range(k , len(nums)):
            count[nums[i]] += 1

            while count[nums[i]] > k  and l < i :
                count[nums[l]] -= 1 
                l += 1

            ans = max(ans , i - l + 1)

        return ans



        