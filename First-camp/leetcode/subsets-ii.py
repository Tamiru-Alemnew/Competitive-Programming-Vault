class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        seen = set()
        nums.sort()
        def backtrack(i , path):
            if tuple(path) not in seen:
                ans.append(path[:])
                seen.add(tuple(path))

            if i >= len(nums):
                return 

            for i in range(i , len(nums)):
                path.append(nums[i])
                backtrack(i+1 , path)
                path.pop()
            
        backtrack(0,[]) 

        return ans 


        