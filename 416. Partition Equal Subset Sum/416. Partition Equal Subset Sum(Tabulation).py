class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False

        half_sum = total_sum / 2

        dp_arr = [[False for _ in range(half_sum + 1)] for _ in range(size)]

        for i in range(size):
            dp_arr[i][0] = True

        if nums[0] <= half_sum:
            dp_arr[0][nums[0]] = True

        for idx in range(1, size):
            for target in range(1, half_sum + 1):
                not_take = dp_arr[idx - 1][target]
                take = False
                if nums[idx] <= target:
                    take = dp_arr[idx - 1][target - nums[idx]]
                dp_arr[idx][target] = take or not_take
        return dp_arr[size - 1][half_sum]
