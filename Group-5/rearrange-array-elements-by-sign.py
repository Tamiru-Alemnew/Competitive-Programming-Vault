class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = [i for i in nums if i >=0 ]
        n = [ i for i in nums if i <0]
        ans = []
        for i in range(len(nums)//2):
            ans.append(p[i]) 
            ans.append(n[i])
        return ans