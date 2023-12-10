class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before , equal , after = [] , [] , []
        for num in nums:
            if num < pivot: before.append(num)
            elif num == pivot : equal.append(num)
            else: after.append(num)
        return before + equal + after
            
        