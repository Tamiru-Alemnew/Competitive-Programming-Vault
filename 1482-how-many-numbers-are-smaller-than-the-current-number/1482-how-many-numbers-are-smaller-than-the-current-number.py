class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNum = sorted(nums)
        index_dict = {}

        for i , num in enumerate(sortedNum):
            if num not in index_dict:
                index_dict[num] = i
        ans = []

        for i in nums:
            ans.append(index_dict[i])
        return ans