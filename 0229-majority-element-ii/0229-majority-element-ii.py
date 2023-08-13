class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count =Counter(nums)
        ans =[]
        for i in nums:
            if count[i] > len(nums)/3 and i not in ans:
                ans.append(i)
        return ans