class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        max_sum = -10001
        local_sum = 0

        for i in range(size):
            local_sum += nums[i]
            max_sum = max(local_sum, max_sum)
            if local_sum < 0:
                local_sum = 0

        return max_sum