import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        def rec_path(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return sys.maxint
            left = grid[i][j] + rec_path(i, j - 1)
            up = grid[i][j] + rec_path(i - 1, j)
            return min(left, up)

        return (rec_path(row - 1, col - 1))