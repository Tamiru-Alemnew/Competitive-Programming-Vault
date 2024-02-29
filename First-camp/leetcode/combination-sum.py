class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
         
        def backtrack(i , path , sm ):
            if sm == target:
                ans.append(path[:])
                return 
                
            if sm > target:
                return 

            for j in range(i,len(candidates)):
                path.append(candidates[j])
                sm += candidates[j]
                backtrack(j , path ,sm)
                path.pop()
                sm -= candidates[j]

        ans = []
        backtrack(0 , [] , 0)
        return ans 
        