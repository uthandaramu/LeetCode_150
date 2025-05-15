class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp_arr = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
                    dp_arr[i][j] = 1
                else:
                    if obstacleGrid[i][j] == 1:
                        dp_arr[i][j] = 0
                    else:
                        dp_arr[i][j] = dp_arr[i-1][j] + dp_arr[i][j-1]

        return dp_arr[row-1][col-1]