class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l1,l2 = len(nums1),len(nums2)
        left , right = 0,0 
        
        while left < l1 and right < l2:
            if nums1[left] == nums2[right]:
                return nums1[left]
            elif nums1[left] > nums2[right]:
                right +=1
            else:
                left+=1
        return -1