class Solution(object):
    def countNeighbour(self, row_id, col_id):
        count = 0
        for r in range(row_id - 1, row_id + 2):
            for c in range(col_id - 1, col_id + 2):

                if (r == row_id and c == col_id) or (r < 0) or (r >= self.row) or (c < 0) or (c >= self.col) or (
                        self.board[r][c] in [0, 2]):
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