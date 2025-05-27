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

        prev_arr = [False for _ in range(half_sum + 1)]

        prev_arr[0] = True

        if nums[0] <= half_sum:
            prev_arr[nums[0]] = True

        for idx in range(1, size):
            cur_arr = [False for _ in range(half_sum + 1)]
            cur_arr[0] = True
            for target in range(1, half_sum + 1):
                not_take = prev_arr[target]
                take = False
                if nums[idx] <= target:
                    take = prev_arr[target - nums[idx]]
                cur_arr[target] = take or not_take
            prev_arr = cur_arr
        return prev_arr[half_sum]
