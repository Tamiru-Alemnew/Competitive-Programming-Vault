class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq = [0] * (len(nums) + 1)

        for s, e in requests:
            freq[s] += 1
            freq[e + 1] -= 1

        for i in range(1, len(freq)):
            freq[i] += freq[ i - 1]
        
        freq.sort(reverse = True)
        nums.sort(reverse = True)
        ans = 0 
        for i in range(len(nums)):
            ans += freq[i] * nums[i]
            if freq[i] == 0:
                break
        return ans % (10**9 + 7)