class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = lower_b = len(nums)
        first = last = -1

        # lower bound
        start = 0
        end = size - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                lower_b = mid
                end = mid - 1
            else:
                start = mid + 1

        if lower_b == size or nums[lower_b] != target:
            return [first, last]

        # upper bound
        start = 0
        end = size - 1
        upper_b = size

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                upper_b = mid
                end = mid - 1
            else:
                start = mid + 1

        return [lower_b, upper_b - 1]