class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        def find_gcd ( x , y ):
            while y :
                x , y = y  , x % y

            return x
        ans = 0 
        for i in range(len(nums)):
            gcd = nums[i]
            for j in range(i , len(nums)):
                gcd = find_gcd(gcd , nums[j])
                ans += gcd == k

        return ans


