from collections import deque


class Solution(object):
    def squareToDim(self, value):
        r = (value - 1) // self.size
        c = (value - 1) % self.size
        if r % 2:
            c = self.size - (1 + c)
        return r, c

    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        board.reverse()
        self.size = len(board)

        queue_box = deque()
        visited_square = set()

        queue_box.append([1, 0])  # Square, Moves

        while queue_box:
            cur_box, moves = queue_box.popleft()

            for i in range(1, 7):  # Possible Dice Values
                next_box = cur_box + i
                r, c = self.squareToDim(next_box)

                if board[r][c] != -1:
                    next_box = board[r][c]

                if next_box == self.size * self.size:
                    return moves + 1

                if next_box not in visited_square:
                    visited_square.add(next_box)
                    queue_box.append([next_box, moves + 1])

        return -1