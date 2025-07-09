class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        size = len(nums)
        curLong = 0
        maxLong = 0
        lastMin = -10 ** 9

        for i in range(size):
            if nums[i] - 1 == lastMin:
                curLong += 1
            elif nums[i] != lastMin:
                curLong = 1

            lastMin = nums[i]
            maxLong = max(maxLong, curLong)

        return (maxLong)