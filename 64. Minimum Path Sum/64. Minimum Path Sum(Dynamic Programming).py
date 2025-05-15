import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        dp_arr = [[-1 for _ in range(col)] for _ in range(row)]

        def rec_path(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return sys.maxint
            if dp_arr[i][j] == -1:
                left = grid[i][j] + rec_path(i, j - 1)
                up = grid[i][j] + rec_path(i - 1, j)
                dp_arr[i][j] = min(left, up)
            return dp_arr[i][j]

        return (rec_path(row - 1, col - 1))