class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i , path ,seen):

            if len(path) == len(nums):
                ans.append(path[:])
                return 

            for j in range( len(nums)):
                if nums[j] not in seen:
                    path.append(nums[j])
                    seen.add(nums[j])
                    backtrack(j + 1 , path , seen)
                    path.pop()
                    seen.remove(nums[j])

        backtrack(0, [ ], set())
        return ans
        