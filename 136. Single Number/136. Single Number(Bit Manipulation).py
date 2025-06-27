class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        ans = 0
        for bit_place in range(0, 32):
            count = 0
            for element in nums:
                if (element & (1 << bit_place)):
                    count += 1
            if count % 2 == 1:
                ans = ans | (1 << bit_place)

        if ans >= 2 ** 31:
            ans -= 2 ** 32
        return ans