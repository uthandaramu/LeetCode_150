### 36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:  

* Each row must contain the digits 1-9 without repetition.  
* Each column must contain the digits 1-9 without repetition.  
* Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.  

**Note:**

* A Sudoku board (partially filled) could be valid but is not necessarily solvable.  
* Only the filled cells need to be validated according to the mentioned rules.


**Example 1:**

<img src= "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" alt="Alt text" width ="200">

Input: board =   
[["5","3",".",".","7",".",".",".","."]  
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]] 

Output: true  

**Example 2:**

Input: board =   
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]  

Output: false  

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.  
 

**Constraints:**

board.length == 9  
board[i].length == 9  
board[i][j] is a digit 1-9 or '.'.  

```python
from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = defaultdict(set)
        col = defaultdict(set)
        sub_box = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    value = board[i][j]
                    if value in row[i] or value in col[j] or value in sub_box[i//3, j//3]:
                        return False
                    row[i].add(value)
                    col[j].add(value)
                    sub_box[i//3, j//3].add(value)
        return True
```