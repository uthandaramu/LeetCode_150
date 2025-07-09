class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        size = len(nums)

        def recPermute(idx):
            if idx == size:
                result.append(nums[:])
                return

            for j in range(idx, size):
                nums[idx], nums[j] = nums[j], nums[idx]
                recPermute(idx + 1)
                nums[j], nums[idx] = nums[idx], nums[j]

        recPermute(0)
        return (result)