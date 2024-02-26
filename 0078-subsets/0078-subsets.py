class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans =[]
            
        def backtrack(i , path):
            ans.append(path[:])
            if i >= len(nums):
                return 

            for i in range(i , len(nums)):
                path.append(nums[i])
                backtrack(i+1 , path)
                path.pop()
            
        backtrack(0,[]) 
    
        return ans

        