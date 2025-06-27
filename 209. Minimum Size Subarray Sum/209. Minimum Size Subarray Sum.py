class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        out = size + 1
        left = 0
        total = 0
        for right in range(size):
            total += nums[right]
            while total >= target:
                out = min(out, right - left + 1)
                total -= nums[left]
                left += 1

        return out if out != size + 1 else 0