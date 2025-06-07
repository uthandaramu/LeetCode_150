class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        row = len(board)
        col = len(board[0])

        visited_path = set()

        def rec_find(r_id, c_id, letter_id, cur_word):
            if letter_id == len(cur_word):
                return True
            if r_id >= row or c_id >= col or r_id < 0 or c_id < 0 or board[r_id][c_id] != cur_word[letter_id] or (
                    (r_id, c_id) in visited_path):
                return False
            visited_path.add((r_id, c_id))
            result = (rec_find(r_id, c_id - 1, letter_id + 1, cur_word) or
                      rec_find(r_id, c_id + 1, letter_id + 1, cur_word) or
                      rec_find(r_id + 1, c_id, letter_id + 1, cur_word) or
                      rec_find(r_id - 1, c_id, letter_id + 1, cur_word))
            visited_path.remove((r_id, c_id))
            return result

        out_arr = []
        for word in words:
            found = False
            for i in range(row):
                for j in range(col):
                    if rec_find(i, j, 0, word):
                        out_arr.append(word)
                        found = True
                        break
                if found:
                    break

        return (out_arr)