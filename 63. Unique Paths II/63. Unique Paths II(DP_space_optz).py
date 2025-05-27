class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        prev_arr = [0 for _ in range(col)]
        for i in range(row):
            cur_arr = [0 for _ in range(col)]
            for j in range(col):
                if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
                    cur_arr[j] = 1
                else:
                    if obstacleGrid[i][j] == 1:
                        cur_arr[j] = 0
                    else:
                        cur_arr[j] = prev_arr[j] + cur_arr[j-1]
            prev_arr = cur_arr

        return prev_arr[col-1]