class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged: List[int] = nums1 + nums2
        merged.sort()

        mid: int = len(merged) // 2 

        if len(merged) % 2 == 0:
            return (merged[mid] + merged[mid-1]) / 2
        else:
            return merged[mid]