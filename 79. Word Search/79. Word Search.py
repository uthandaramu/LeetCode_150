class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        visited_path = set()

        def rec_search(r, c, letter_idx):

            if letter_idx == len(word):
                return True
            if r >= row or c >= col or r < 0 or c < 0 or word[letter_idx] != board[r][c] or (r, c) in visited_path:
                return False

            visited_path.add((r, c))
            result = (rec_search(r, c + 1, letter_idx + 1) or
                      rec_search(r, c - 1, letter_idx + 1) or
                      rec_search(r - 1, c, letter_idx + 1) or
                      rec_search(r + 1, c, letter_idx + 1))
            visited_path.remove((r, c))
            return result

        for i in range(row):
            for j in range(col):
                if rec_search(i, j, 0):
                    return True
        return False