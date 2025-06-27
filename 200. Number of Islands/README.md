### 200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

Input: grid = [  
  ["1","1","1","1","0"],  
  ["1","1","0","1","0"],  
  ["1","1","0","0","0"],  
  ["0","0","0","0","0"]  
]  
Output: 1

**Example 2:**

Input: grid = [  
  ["1","1","0","0","0"],  
  ["1","1","0","0","0"],  
  ["0","0","1","0","0"],  
  ["0","0","0","1","1"]  
]  
Output: 3
 

**Constraints:**

* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 300
* grid[i][j] is '0' or '1'.

```python
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
            
            #out of bound
            if row_id >= row or col_id >= col or row_id < 0 or col_id < 0:
                return
            
            #Already visited node or water node
            if grid[row_id][col_id] == "0" or visited[row_id][col_id] == 1:
                return
            
            #marking the current node as visited
            visited[row_id][col_id] = 1

            #Exploring in all four directions
            connectIsland(row_id-1, col_id)
            connectIsland(row_id, col_id-1)
            connectIsland(row_id, col_id+1)
            connectIsland(row_id+1, col_id)
        
            
        num_isLand = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    connectIsland(i, j)
                    num_isLand += 1
        
        return num_isLand
```