### 289. Game of Life

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

* Any live cell with fewer than two live neighbors dies as if caused by under-population.
* Any live cell with two or three live neighbors lives on to the next generation.
* Any live cell with more than three live neighbors dies, as if by over-population.
* Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
* The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

**Example 1:**



**Input:** board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]  
**Output:** [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

**Example 2:**


**Input:** board = [[1,1],[1,0]]  
**Output:** [[1,1],[1,1]]

**Constraints:**

* m == board.length
* n == board[i].length
* 1 <= m, n <= 25
* board[i][j] is 0 or 1.

**Follow up:**

* Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
* In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

### Additional Space approach (not preferable)

```python
class Solution(object):
    def countNeighbour(self, row_id, col_id):
        count = 0
        for r in range(row_id-1, row_id+2):
            for c in range(col_id-1, col_id+2):
                if (r == row_id and c == col_id) or (r < 0) or (r >= self.row) or (c < 0) or (c >= self.col) or (self.board[r][c] == 0):
                    continue
                
                count += 1

        return count


    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board

        self.row = len(board)
        self.col = len(board[0])

        markArr = [[0 for _ in range(self.col)] for _ in range(self.row)]

        for r in range(self.row):
            for c in range(self.col):
                neighbourLives = self.countNeighbour(r, c)

                if self.board[r][c]:
                    if neighbourLives in [2, 3]:
                        markArr[r][c] = 1

                else:
                    if neighbourLives == 3:
                        markArr[r][c] = 1
        
        for i in range(self.row):
            for j in range(self.col):
                board[i][j] = markArr[i][j]
```

### With No Additional memory (Optimized and preferable)

#### Below representation table is used to make this code work in place

| Original | Converted | Representation |
|:--------:|:---------:|:--------------:|
|    0     |     0     |       0        |
|    0     |     1     |       2        |
|    1     |     0     |       1        |
|    1     |     1     |       3        |


```python
class Solution(object):
    def countNeighbour(self, row_id, col_id):
        count = 0
        for r in range(row_id-1, row_id+2):
            for c in range(col_id-1, col_id+2):
                
                if (r == row_id and c == col_id) or (r < 0) or (r >= self.row) or (c < 0) or (c >= self.col) or (self.board[r][c] in [0, 2]):
                    continue
                
                count += 1

        return count


    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        """
        Original -> Converted = Representation
        ---------------------------------------
            0    ->     0     =       0    
            0    ->     1     =       2  
            1    ->     0     =       1
            1    ->     1     =       3   
        """

        self.board = board

        self.row = len(board)
        self.col = len(board[0])

        for r in range(self.row):
            for c in range(self.col):
                neighbourLives = self.countNeighbour(r, c)

                if self.board[r][c] in [1, 3]:
                    if neighbourLives in [2, 3]:
                        self.board[r][c] = 3
                    
                    elif neighbourLives > 3:
                        self.board[r][c] = 1
                
                else:
                    if neighbourLives == 3:
                        self.board[r][c] = 2
        
        
        for i in range(self.row):
            for j in range(self.col):

                if self.board[i][j] in [2, 3]:
                    self.board[i][j] = 1
                
                elif self.board[i][j] == 1:
                    self.board[i][j] = 0
```