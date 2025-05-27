### 62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" width="400">

Input: m = 3, n = 7  
Output: 28

**Example 2:**

Input: m = 3, n = 2  
Output: 3  
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

**Constraints:**

1 <= m, n <= 100

### With Recursion

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def core_rec(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            up = core_rec(i - 1, j)
            left = core_rec(i, j - 1)
            return (up + left)

        return (core_rec(m - 1, n - 1))
```

### With Dynamic Programming

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp_arr = [[-1 for _ in range(n)] for _ in range(m)]
        def core_rec(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if dp_arr[i][j] == -1:
                up = core_rec(i-1, j)
                left = core_rec(i, j-1)
                dp_arr[i][j] = up + left
            return dp_arr[i][j]

        return(core_rec(m-1,n-1))
```

### With Dynamic Programming (Tabulation)

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp_arr = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp_arr[i][j] = 1
                else:
                    dp_arr[i][j] = dp_arr[i-1][j] + dp_arr[i][j-1]
        
        return dp_arr[m-1][n-1]
```

### With Dynamic Programming (Space Optimized)

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prev_arr = [0 for _ in range(n)]
        for i in range(m):
            cur_arr = [0 for _ in range(n)]
            for j in range(n):
                if i == 0 and j == 0:
                    cur_arr[j] = 1
                else:
                    cur_arr[j] = prev_arr[j] + cur_arr[j-1]
            prev_arr=cur_arr
        
        return (prev_arr[n-1])
```