class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        start, end, i = 0, n - 1, n - 1
        while start <= end:
            start_sq = nums[start] ** 2
            end_sq = nums[end] ** 2
            if start_sq > end_sq:
                res[i] = start_sq
                start += 1
            else:
                res[i] = end_sq
                end -= 1
            i -= 1
        return res



                
        