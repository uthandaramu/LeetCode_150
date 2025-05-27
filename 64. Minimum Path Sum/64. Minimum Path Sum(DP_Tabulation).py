import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        dp_arr = [[sys.maxint for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp_arr[i][j] = grid[i][j]
                else:
                    left = grid[i][j] + dp_arr[i][j - 1]
                    up = grid[i][j] + dp_arr[i - 1][j]
                    dp_arr[i][j] = min(left, up)

        return dp_arr[row - 1][col - 1]