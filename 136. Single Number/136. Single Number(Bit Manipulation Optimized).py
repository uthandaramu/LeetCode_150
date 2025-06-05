class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bucket Approach
        # Element will go to ones if it is not in twos
        # Element will go to twos(ignorable) if it is in ones
        ones = 0
        for element in nums:
            ones = (ones ^ element) & (~0)

        return ones