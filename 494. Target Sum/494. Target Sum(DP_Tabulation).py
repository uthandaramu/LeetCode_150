class Solution(object):
    def helper(self, index, target):
        if self.nums[0] == 0:
            self.dp_arr[0][0] = 2
        else:
            self.dp_arr[0][0] = 1

        if self.nums[0] != 0 and self.nums[0] <= target:
            self.dp_arr[0][self.nums[0]] = 1

        for idx in range(1, index + 1):
            for tar in range(target + 1):
                not_take = self.dp_arr[idx - 1][tar]
                take = 0
                if self.nums[idx] <= tar:
                    take = self.dp_arr[idx - 1][tar - self.nums[idx]]
                self.dp_arr[idx][tar] = take + not_take
        return self.dp_arr[index][target]

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = nums
        self.target = target
        self.total_sum = sum(nums)
        self.size = len(nums)

        self.dp_arr = [[0 for _ in range(((self.total_sum - self.target) // 2) + 1)] for _ in range(self.size)]

        if (self.total_sum - self.target) >= 0 and (self.total_sum - self.target) % 2 == 0:
            return self.helper(self.size - 1, (self.total_sum - self.target) // 2)
        else:
            return 0