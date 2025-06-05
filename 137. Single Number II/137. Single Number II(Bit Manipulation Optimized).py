class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0

        # element goes to ones if it is not in twos
        # element goes to twos if it is in ones
        # element goes to threes(no need) if it is in twos
        # Basically I need two operations, one is to add and other is to remove

        for element in nums:
            ones = (ones ^ element) & (~twos)
            twos = (twos ^ element) & (~ones)

        return ones