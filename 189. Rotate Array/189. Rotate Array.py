class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        no_rota = k % size
        part = size-no_rota
        num_1 = nums[part:]
        num_2 = nums[:part]
        nums[:] = num_1 + num_2