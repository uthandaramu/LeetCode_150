### 51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" width="350">

Input: n = 4  
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]  
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

**Example 2:**

Input: n = 1  
Output: [["Q"]]

**Constraints:**

* 1 <= n <= 9

```python
class Solution(object):
    def isSafe(self, r_id, c_id, board):
        row = col = self.n
        row_cpy = r_id
        col_cpy = c_id

        #check staright left
        while c_id >= 0:
            if board[r_id][c_id] == "Q":
                return False
            c_id -= 1

        c_id = col_cpy
        
        #check up diagonal
        while r_id >= 0 and c_id >= 0:
            if board[r_id][c_id] == "Q":
                return False
            r_id -= 1
            c_id -= 1
        
        r_id = row_cpy
        c_id = col_cpy

        #check bottom diagonal
        while r_id < row  and col >= 0:
            if board[r_id][c_id] == "Q":
                return False
            r_id += 1
            c_id -= 1
        
        return True


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = row = col = n

        board = ["." * col for _ in range(row)]

        out = []

        def placeQueen(c_id):
            if c_id == col:
                out.append(board[:])
                return
            for r_id in range(row):    
                if self.isSafe(r_id, c_id, board):
                    board[r_id] = board[r_id][:c_id] + "Q" + "".join(board[r_id][c_id + 1 :])
                    placeQueen(c_id+1)
                    board[r_id] = board[r_id][:c_id] + "." + "".join(board[r_id][c_id + 1 :])
        
        placeQueen(0)

        return (out)
```