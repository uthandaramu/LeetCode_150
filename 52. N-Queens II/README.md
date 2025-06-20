### 52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.


**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" width="350">

Input: n = 4  
Output: 2  
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

**Example 2:**

Input: n = 1  
Output: 1
 

**Constraints:**

* 1 <= n <= 9

```python
class Solution(object):
    def isSafe(self, row_id, col_id, board):
        row = len(board)
        col = len(board[0])
        row_cpy = row_id
        col_cpy = col_id

        #check stright left
        while col_id >= 0:
            if board[row_id][col_id] == "Q":
                return False
            col_id -= 1
        
        col_id = col_cpy

        #check up diagonal
        while row_id >= 0 and col_id >= 0:
            if board[row_id][col_id] == "Q":
                return False
            row_id -= 1
            col_id -= 1
        
        row_id = row_cpy
        col_id = col_cpy

        #check bottom diagonal
        while row_id < row and col_id >= 0:
            if board[row_id][col_id] == "Q":
                return False
            row_id += 1
            col_id -= 1
        
        return True

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = col = n

        board = [[0 for _ in range(col)] for _ in range(row)]

        self.out = 0

        def placeQueen(c_id):
            if c_id == col:
                self.out += 1
                return
            for r_id in range(row):
                if self.isSafe(r_id, c_id, board):
                    board[r_id][c_id] = "Q"
                    placeQueen(c_id+1)
                    board[r_id][c_id] = 0

        placeQueen(0)
        return self.out
```