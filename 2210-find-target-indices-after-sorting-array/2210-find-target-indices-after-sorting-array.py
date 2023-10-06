class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l = t = 0   
        ans = []
        for i in nums:
            if i == target:
                t += 1
            elif i < target:
                l += 1 
        for i in range(t):
            ans.append(l)
            l += 1
        return ans
