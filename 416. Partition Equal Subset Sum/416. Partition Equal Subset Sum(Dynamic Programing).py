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

        def rec_partition(idx, target):
            if target == 0:
                return True
            if idx == 0:
                return nums[idx] == target
            if dp_arr[idx][target] == -1:
                not_take = rec_partition(idx-1, target)
                take = False
                if nums[idx] <= target:
                    take = rec_partition(idx-1, target - nums[idx])
                dp_arr[idx][target] = take or not_take
            return dp_arr[idx][target]

        return (rec_partition(size-1, half_sum))