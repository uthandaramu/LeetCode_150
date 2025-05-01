class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j, k, i = m - 1, n - 1, m + n - 1
        while j >= 0 and k >= 0 and i >= 0:
            if nums1[j] >= nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                nums1[i] = nums2[k]
                k -= 1
            i -= 1
        while k >= 0:
            nums1[i] = nums2[k]
            k -= 1
            i -= 1
        while j >= 0:
            nums1[i] = nums1[j]
            j -= 1
            i -= 1