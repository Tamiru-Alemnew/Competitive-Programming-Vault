# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        n = len(nums)

        for mask in range(1<<n):
            subset = []

            for indx in range(n):
                if (1 << indx)&mask:
                    subset.append(nums[indx])
            
            ans.append(subset)
            
        return ans