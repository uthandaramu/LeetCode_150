class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = set(nums)
        maxCount = 0

        for val in elements:
            curCount = 1
            if val - 1 not in elements:
                while val + 1 in elements:
                    curCount += 1
                    val = val + 1

            maxCount = max(curCount, maxCount)

        return (maxCount)