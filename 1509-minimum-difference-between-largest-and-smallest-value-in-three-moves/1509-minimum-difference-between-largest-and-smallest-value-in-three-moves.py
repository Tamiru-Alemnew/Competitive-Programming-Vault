class Solution:
    def minDifference(self, nums: List[int]) -> int:
        partial_min = [float('-inf')]*4
        partial_max =[float('-inf')]*4

        if len(nums) <= 4:
            return 0

        for n in nums:
            if -partial_min[0] > n:
                heappop(partial_min)
                heappush(partial_min , -n)

            if partial_max[0] < n :
                heappop(partial_max)
                heappush(partial_max , n)

        ans = float("inf")
        for n in range(4):
            mn = heappop(partial_min)
            heappush(partial_min , -mn)

        for i in range(4):
            mn = heappop(partial_min)
            mx = heappop(partial_max)
            ans = min(ans , abs(mx - mn))

        return ans
            