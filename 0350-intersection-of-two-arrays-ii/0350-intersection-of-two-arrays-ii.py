class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        ans = []

        for num in freq1.keys():
            if num in freq2:
                ans.extend([num for i in range(min(freq1[num ] , freq2[num]))])

        return ans 