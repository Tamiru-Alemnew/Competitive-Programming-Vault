class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ps = 0
        ps_count ={0:1}
        ans = 0
        for num in nums:
            if num % 2:
                ps += 1
            ans += ps_count.get(ps-k , 0)
            ps_count[ps] = ps_count.get(ps , 0) + 1

        return ans 