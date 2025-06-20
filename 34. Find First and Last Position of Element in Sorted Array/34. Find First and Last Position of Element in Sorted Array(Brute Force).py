class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        first = last = -1

        for i in range(size):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i

        return [first, last]