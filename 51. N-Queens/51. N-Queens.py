class Solution(object):
    def isSafe(self, r_id, c_id, board):
        row = col = self.n
        row_cpy = r_id
        col_cpy = c_id

        # check staright left
        while c_id >= 0:
            if board[r_id][c_id] == "Q":
                return False
            c_id -= 1

        c_id = col_cpy

        # check up diagonal
        while r_id >= 0 and c_id >= 0:
            if board[r_id][c_id] == "Q":
                return False
            r_id -= 1
            c_id -= 1

        r_id = row_cpy
        c_id = col_cpy

        # check bottom diagonal
        while r_id < row and col >= 0:
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
                    board[r_id] = board[r_id][:c_id] + "Q" + "".join(board[r_id][c_id + 1:])
                    placeQueen(c_id + 1)
                    board[r_id] = board[r_id][:c_id] + "." + "".join(board[r_id][c_id + 1:])

        placeQueen(0)

        return (out)