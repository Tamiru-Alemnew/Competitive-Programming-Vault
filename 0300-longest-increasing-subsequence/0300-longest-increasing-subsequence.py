class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        dp = [1 for i in range(len(arr))]
        ans = 1
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i] , dp[j] + 1)
                    ans = max(ans ,dp[i])

        return ans