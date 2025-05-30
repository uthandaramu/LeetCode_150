class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = nums[0]
        size = len(nums)
        start, end = 1, size - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > minimum:
                start = mid + 1
            elif nums[mid] < minimum:
                end = mid - 1
            minimum = min(minimum, nums[mid])

        return minimum