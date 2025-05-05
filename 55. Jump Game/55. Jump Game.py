class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        max_index = 0
        for i in range(length-1):
            if i > max_index:
                return False
            max_index = max(max_index, i+nums[i])
        return max_index >= length-1