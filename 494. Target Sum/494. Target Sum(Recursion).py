class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)
        size = len(nums)

        def rec_sum(idx, target):
            if idx == 0:
                if target == 0 and nums[idx] == 0:
                    return 2
                if target == 0 or nums[idx] == target:
                    return 1
                return 0

            not_pick = rec_sum(idx - 1, target)
            pick = 0
            if nums[idx] <= target:
                pick = rec_sum(idx - 1, target - nums[idx])
            return (pick + not_pick)

        if (total_sum - target) >= 0 and (total_sum - target) % 2 == 0:
            return rec_sum(size - 1, (total_sum - target) / 2)
        else:
            return 0