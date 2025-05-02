class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 2
        size = len(nums)
        if size <= 2:
            return size
        while i < size:
            if (nums[i] == nums[i-1] and nums[i] == nums[i-2]):
                nums.pop(i)
                size -= 1
                continue
            i += 1
        return size