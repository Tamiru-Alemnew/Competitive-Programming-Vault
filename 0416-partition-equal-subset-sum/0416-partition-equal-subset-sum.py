class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1 :
            return False

        md = total // 2
        dp = [False]*(md+1)
        dp[0] = True

        for a in nums:
            for i in range(md , -1 , -1):
                if i -a >= 0 :
                    dp[i] = dp[i] or dp[i-a]

        print(dp)
        return dp[md]



        