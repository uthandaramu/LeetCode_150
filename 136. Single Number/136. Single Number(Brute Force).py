class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        size = len(nums)
        out = None
        for i in range(1, size, 2):
            if nums[i-1] != nums[i]:
                out = nums[i-1]
                break
        if out is None:
            out = nums[-1]
        return out