### 130. Surrounded Regions

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.  
Region: To form a region connect every 'O' cell.  
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.  
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.  

**Example 1:**

**Input:** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

**Output:** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

**Explanation:**

<img src="https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg" width="400">

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

**Example 2:**

**Input:** board = [["X"]]

**Output:** [["X"]]

**Constraints:**

* m == board.length
* n == board[i].length
* 1 <= m, n <= 200
* board[i][j] is 'X' or 'O'.

```python
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        visited = [[0 for _ in range(col)] for _ in range(row)]

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            if board[r][c] == "O" and visited[r][c] == 0:
                visited[r][c] = 1
                dfs(r, c+1)
                dfs(r, c-1)
                dfs(r-1, c)
                dfs(r+1, c)
            else:
                return
        
        for c in range(col):
            dfs(0, c)
            dfs(row-1, c)
        
        for r in range(row):
            dfs(r, 0)
            dfs(r, col-1)

        for i in range(row):
            for j in range(col):
                if visited[i][j] == 0:
                    board[i][j] = "X"
```