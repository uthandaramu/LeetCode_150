class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        def rec_cherry(i, j1, j2):
            if j1 > col-1 or j2 > col-1 or j1 < 0 or j2 < 0:
                return -1
            if i == row-1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            maxi = 0
            for dj1 in range(-1, 2):
                for dj2 in range(-1, 2):
                    if j1 == j2:
                        cur_val = grid[i][j1] + rec_cherry(i+1, j1+dj1, j2+dj2)
                    else:
                        cur_val = grid[i][j1] + grid[i][j2] + rec_cherry(i+1, j1+dj1, j2+dj2)
                    maxi = max(maxi, cur_val)
            return maxi

        return(rec_cherry(0, 0, col-1))