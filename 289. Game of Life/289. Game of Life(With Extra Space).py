class Solution(object):
    def countNeighbour(self, row_id, col_id):
        count = 0
        for r in range(row_id - 1, row_id + 2):
            for c in range(col_id - 1, col_id + 2):
                if (r == row_id and c == col_id) or (r < 0) or (r >= self.row) or (c < 0) or (c >= self.col) or (
                        self.board[r][c] == 0):
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