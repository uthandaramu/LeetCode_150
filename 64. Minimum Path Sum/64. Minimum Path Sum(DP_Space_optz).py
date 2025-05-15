import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        prev_arr = [sys.maxint for _ in range(col)]
        for i in range(row):
            cur_arr = [sys.maxint for _ in range(col)]
            for j in range(col):
                if i == 0 and j == 0:
                    cur_arr[j] = grid[i][j]
                else:
                    left = grid[i][j] + cur_arr[j-1]
                    up = grid[i][j] + prev_arr[j]
                    cur_arr[j] = min(left, up)
            prev_arr = cur_arr

        return prev_arr[col-1]