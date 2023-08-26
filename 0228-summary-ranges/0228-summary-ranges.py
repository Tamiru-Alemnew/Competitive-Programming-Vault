class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) <= 1:
            return [f'{num}' for num in nums]

        res = []
        pre = start = nums[0]

        for i in nums[1:]:
            if i - pre != 1:
                res.append(f'{start}->{pre}' if pre - start > 0 else f'{pre}')
                start = i
            pre = i

        res.append(f'{start}->{pre}' if pre - start > 0 else f'{pre}')
        return res
