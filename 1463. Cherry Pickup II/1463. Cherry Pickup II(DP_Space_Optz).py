class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        prev_arr = [[-1 for _ in range(col)] for _ in range(col)]

        #Base Case
        for j1 in range(col):
            for j2 in range(col):
                if j1 == j2:
                    prev_arr[j1][j2] = grid[row-1][j1]
                else:
                    prev_arr[j1][j2] = grid[row-1][j1] + grid[row-1][j2]
        #dp_arr iteration
        for i in range(row-2, -1, -1):
            cur_arr = [[-1 for _ in range(col)] for _ in range(col)]
            for j1 in range(col):
                for j2 in range(col):
                    #finding max from all possible ways
                    maxi = 0
                    for dj1 in range(-1, 2):
                        for dj2 in range(-1, 2):
                            if j1+dj1 >= 0 and j1+dj1 < col and j2+dj2 >= 0 and j2+dj2 < col:
                                if j1 == j2:
                                    cur_val = grid[i][j1] + prev_arr[j1+dj1][j2+dj2]
                                else:
                                    cur_val = grid[i][j1] + grid[i][j2] + prev_arr[j1+dj1][j2+dj2]
                            else:
                                cur_val = -1
                            maxi = max(maxi, cur_val)
                    cur_arr[j1][j2] = maxi
            prev_arr = cur_arr

        return prev_arr[0][col-1]