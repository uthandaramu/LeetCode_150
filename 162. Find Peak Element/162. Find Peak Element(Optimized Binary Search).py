class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)

        # Edge Case for 1 element
        if size == 1:
            return 0

        # Edge cases for corner elements
        if nums[0] > nums[1]:
            return 0

        if nums[size - 1] > nums[size - 2]:
            return (size - 1)

        # Binary search for the rest of the elements
        start = 1
        end = size - 2

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] > nums[mid - 1]:
                start = mid + 1

            elif nums[mid - 1] > nums[mid]:
                end = mid - 1