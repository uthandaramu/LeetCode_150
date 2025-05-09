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