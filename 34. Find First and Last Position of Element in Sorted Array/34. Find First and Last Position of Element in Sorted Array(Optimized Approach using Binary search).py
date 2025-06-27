class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Plain binary search approach

        size = len(nums)

        first = last = -1

        start, end = 0, size - 1

        # Identify first occurrence
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                first = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        if first == -1:
            return [first, last]

        # Identify last occurrence
        start, end = first, size - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                start = mid + 1
                last = mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return [first, last]