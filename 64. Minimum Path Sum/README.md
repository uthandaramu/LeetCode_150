### 64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg">

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]  
Output: 7  
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

**Example 2:**

Input: grid = [[1,2,3],[4,5,6]]  
Output: 12

**Constraints:**

m == grid.length  
n == grid[i].length  
1 <= m, n <= 200  
0 <= grid[i][j] <= 200

### With Recursion

```python
import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        def rec_path(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return sys.maxint
            left = grid[i][j] + rec_path(i, j-1)
            up = grid[i][j] + rec_path(i-1, j)
            return min(left, up)
        
        return (rec_path(row-1, col-1))
```

### With Dynamic Programming

```python
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
                left = grid[i][j] + rec_path(i, j-1)
                up = grid[i][j] + rec_path(i-1, j)
                dp_arr[i][j] = min(left, up)
            return dp_arr[i][j]
        
        return (rec_path(row-1, col-1))
```

### With Dynamic Programming (Tabulation)

```python
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
                    left = grid[i][j] + dp_arr[i][j-1]
                    up = grid[i][j] + dp_arr[i-1][j]
                    dp_arr[i][j] = min(left, up)
        
        return dp_arr[row-1][col-1]
```

### With Dynamic Programming (Space Optimized)

```python
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
```