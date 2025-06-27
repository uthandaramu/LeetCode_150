class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        nums.sort()
        out = None
        for i in range(1, size, 3):
            if nums[i-1] != nums[i]:
                out = nums[i-1]
                break
        if out is None:
            out = nums[-1]
        return out