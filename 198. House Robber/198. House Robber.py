class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        out_arr = [0] * len(nums)
        temp = 0
        out_arr[0] = nums[0]
        out_arr[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = nums[i] + out_arr[i - 2]
            out_arr[i] = max(temp, out_arr[i - 1])

        return out_arr[-1]