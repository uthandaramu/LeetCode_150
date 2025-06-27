class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        total = 0
        global_min = nums[0]
        global_max = nums[0]
        cur_min = cur_max = 0
        for i in range(0, size):
            total += nums[i]
            cur_min = min(cur_min + nums[i], nums[i])
            cur_max = max(cur_max + nums[i], nums[i])
            global_min = min(cur_min, global_min)
            global_max = max(cur_max, global_max)

        return (max(global_max, total-global_min)) if global_max > 0 else global_max