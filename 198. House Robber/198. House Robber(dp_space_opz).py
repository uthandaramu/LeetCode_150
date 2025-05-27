class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        prev = nums[0]
        prev2 = 0
        for i in range(1, size):
            take = nums[i] + prev2
            non_take = 0 + prev
            cur_max = max(take, non_take)
            prev2 = prev
            prev = cur_max
        return prev