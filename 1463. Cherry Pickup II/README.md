### 1463. Cherry Pickup II

You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.  

You have two robots that can collect cherries for you:  

Robot #1 is located at the top-left corner (0, 0), and  
Robot #2 is located at the top-right corner (0, cols - 1).  
Return the maximum number of cherries collection using both robots by following the rules below:  

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).  
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.  
When both robots stay in the same cell, only one takes the cherries.  
Both robots cannot move outside of the grid at any moment.  
Both robots should reach the bottom row in grid.  

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/04/29/sample_1_1802.png">

Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]  
Output: 24  
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.  
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.  
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.  
Total of cherries: 12 + 12 = 24.  

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/04/23/sample_2_1802.png">

Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]  
Output: 28  
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.  
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.  
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.  
Total of cherries: 17 + 11 = 28.  

**Constraints:**

rows == grid.length  
cols == grid[i].length  
2 <= rows, cols <= 70  
0 <= grid[i][j] <= 100  

### With Recursion

```python
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
```

### With Dynamic Programming

```python
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        dp_arr = [[[-1 for _ in range(col)] for _ in range(col)] for _ in range(row)]
        def rec_cherry(i, j1, j2):
            if j1 > col-1 or j2 > col-1 or j1 < 0 or j2 < 0:
                return -1
            if i == row-1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            if dp_arr[i][j1][j2] == -1:
                maxi = 0
                for dj1 in range(-1, 2):
                    for dj2 in range(-1, 2):
                        if j1 == j2:
                            cur_val = grid[i][j1] + rec_cherry(i+1, j1+dj1, j2+dj2)
                        else:
                            cur_val = grid[i][j1] + grid[i][j2] + rec_cherry(i+1, j1+dj1, j2+dj2)
                        maxi = max(maxi, cur_val)
                dp_arr[i][j1][j2] = maxi
            return dp_arr[i][j1][j2]

        return(rec_cherry(0, 0, col-1))
```

### With Dynamic Programming (Tabulation)

```python
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        dp_arr = [[[-1 for _ in range(col)] for _ in range(col)] for _ in range(row)]

        #Base Case
        for j1 in range(col):
            for j2 in range(col):
                if j1 == j2:
                    dp_arr[row-1][j1][j2] = grid[row-1][j1]
                else:
                    dp_arr[row-1][j1][j2] = grid[row-1][j1] + grid[row-1][j2]
        #dp_arr iteration
        for i in range(row-2, -1, -1):
            for j1 in range(col):
                for j2 in range(col):
                    #finding max from all possible ways
                    maxi = 0
                    for dj1 in range(-1, 2):
                        for dj2 in range(-1, 2):
                            if j1+dj1 >= 0 and j1+dj1 < col and j2+dj2 >= 0 and j2+dj2 < col:
                                if j1 == j2:
                                    cur_val = grid[i][j1] + dp_arr[i+1][j1+dj1][j2+dj2]
                                else:
                                    cur_val = grid[i][j1] + grid[i][j2] + dp_arr[i+1][j1+dj1][j2+dj2]
                            else:
                                cur_val = -1
                            maxi = max(maxi, cur_val)
                    dp_arr[i][j1][j2] = maxi

        return dp_arr[0][0][col-1]
```

### With Dynamic Programming (Space Optimized)

```python
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
```