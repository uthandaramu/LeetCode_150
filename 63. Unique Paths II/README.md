### 63. Unique Paths II

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg">

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]  
Output: 2  
Explanation: There is one obstacle in the middle of the 3x3 grid above.  
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg">

Input: obstacleGrid = [[0,1],[0,0]]  
Output: 1
 

**Constraints:**

m == obstacleGrid.length  
n == obstacleGrid[i].length  
1 <= m, n <= 100  
obstacleGrid[i][j] is 0 or 1.

### With Recursion

```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        def recur_path(i, j):
            if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
                return 1
            if i<0 or j<0: 
                return 0
            if i < row and j < col and obstacleGrid[i][j] == 1:
                return 0
            up = recur_path(i-1, j)
            left = recur_path(i, j-1)
            return (up+left)
        
        return recur_path(row-1, col-1)
```
### WIth Dynamic Programming

```python
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
            if i<0 or j<0: 
                return 0
            if i < row and j < col and obstacleGrid[i][j] == 1:
                return 0
            if dp_arr[i][j] == -1:
                up = recur_path(i-1, j)
                left = recur_path(i, j-1)
                dp_arr[i][j] = up + left
            return dp_arr[i][j]
        
        return recur_path(row-1, col-1)
```

### With Dynamic Programming(Tabulation)

```python
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
```

### With Dynamic Programming(Space optimized)

```python
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
```