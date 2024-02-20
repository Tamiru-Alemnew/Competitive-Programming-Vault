class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums1)

        for num2 in nums2:
            
            while stack and nums1[stack[-1]] < num2:
                idx = stack.pop()
                res[idx] = num2
            if num2 in nums1:
                stack.append(nums1.index(num2))
        
        return res