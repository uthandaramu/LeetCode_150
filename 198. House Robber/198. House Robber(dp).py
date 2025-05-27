class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp_arr = [-1]*(size)
        def dp_rob(cur_idx):
            if cur_idx >= size:
                return 0
            if dp_arr[cur_idx] == -1:
                pick = nums[cur_idx] + dp_rob(cur_idx+2)
                not_pick = dp_rob(cur_idx+1)
                dp_arr[cur_idx] = max(pick, not_pick)
            return dp_arr[cur_idx]
        return dp_rob(0)