class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = n
        out = 0
        while x >= 5:
            out += x // 5
            x = x // 5

        return out