class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def core_rec(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            up = core_rec(i - 1, j)
            left = core_rec(i, j - 1)
            return (up + left)

        return (core_rec(m - 1, n - 1))