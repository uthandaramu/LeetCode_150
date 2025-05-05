class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_index = jump = end = 0
        size = len(nums)
        left = right = farthest = 0
        while right < size-1:
            for i in range(left, right+1):
                farthest = max(farthest, i+nums[i])
            left = right+1
            right = farthest
            jump+=1
        return jump