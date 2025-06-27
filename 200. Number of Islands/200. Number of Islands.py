class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        visited = [[0 for _ in range(col)] for _ in range(row)]

        def connectIsland(row_id, col_id):

            # out of bound
            if row_id >= row or col_id >= col or row_id < 0 or col_id < 0:
                return

            # Already visited node or water node
            if grid[row_id][col_id] == "0" or visited[row_id][col_id] == 1:
                return

            # marking the current node as visited
            visited[row_id][col_id] = 1

            # Exploring in all four directions
            connectIsland(row_id - 1, col_id)
            connectIsland(row_id, col_id - 1)
            connectIsland(row_id, col_id + 1)
            connectIsland(row_id + 1, col_id)

        num_isLand = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    connectIsland(i, j)
                    num_isLand += 1

        return num_isLand