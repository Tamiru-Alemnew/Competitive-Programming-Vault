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

        largest = sorted([x for x in partial_max])
        smallest = sorted([-x for x in partial_min])

        for i in range(4):
            ans = min(ans , largest[i] - smallest[i])

        return ans
            