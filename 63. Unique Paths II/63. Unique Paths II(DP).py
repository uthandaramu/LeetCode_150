class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp_arr = [[-1 for _ in range(col)] for _ in range(row)]

        def recur_path(i, j):
            if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
                return 1
            if i < 0 or j < 0:
                return 0
            if i < row and j < col and obstacleGrid[i][j] == 1:
                return 0
            if dp_arr[i][j] == -1:
                up = recur_path(i - 1, j)
                left = recur_path(i, j - 1)
                dp_arr[i][j] = up + left
            return dp_arr[i][j]

        return recur_path(row - 1, col - 1)