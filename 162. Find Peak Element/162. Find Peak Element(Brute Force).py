class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = peak = 0
        size = len(nums)

        for i in range(size):
            if (i == 0 or nums[i-1] < nums[i]) and (i == size-1 or nums[i] > nums[i+1]):
                return i