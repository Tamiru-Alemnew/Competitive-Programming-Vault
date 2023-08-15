class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        indxFinder ={n:i for i,n in enumerate(nums1)}
        res = [-1]*len(nums1)

        for i in range(len(nums2)):

            cur = nums2[i]
            while stack and cur > stack[-1]:
                ind = indxFinder[stack.pop()]
                res[ind] = cur

            if cur in nums1:
                stack.append(cur)

        return res