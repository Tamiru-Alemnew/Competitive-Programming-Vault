class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        cur = 0 
        ans = 0 
        for  val in freq.values():
            if val == cur :
                ans += val
            elif val > cur:
                ans = val
                cur = val 

        return ans 

        