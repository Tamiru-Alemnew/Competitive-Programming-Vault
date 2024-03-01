class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(nums, cur_sum, slot):
            if slot == 0: 
                if cur_sum == n:
                    res.append(nums)
                return
            num = 1 if len(nums)==0 else nums[-1]+1
            while num <= 9:
                if num + cur_sum <= n:
                    backtrack(nums + [num], num + cur_sum, slot-1)
                else:
                    return
                num += 1
        backtrack([], 0, k)
        return res