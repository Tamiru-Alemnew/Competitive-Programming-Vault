class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        if len(nums1) >len(nums2):
            return [i for i in nums1 if i in nums2]
        else:
            return [i for i in nums2 if i in nums1]
        