class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        right1 = m - 1
        right2 = n - 1
        right = m + n - 1

        while right1 >= 0 and right2 >= 0:
            if nums1[right1] > nums2[right2]:
                nums1[right] = nums1[right1]
                right1 -= 1
            else:
                nums1[right] = nums2[right2]
                right2 -= 1
            right -= 1

        # Handle remaining elements in nums2 (if any)
        while right2 >= 0:
            nums1[right] = nums2[right2]
            right -= 1
            right2 -= 1
