class Solution:
    def maximumPath(self, mat):
        # code here
        row = len(mat)
        col = len(mat[0])

        def rec_max(i, j):
            if i < 0 or j < 0 or i > row - 1 or j > col - 1:
                return 0
            if i == row - 1:
                return mat[i][j]
            down = mat[i][j] + rec_max(i + 1, j)
            left_diagnol = mat[i][j] + rec_max(i + 1, j - 1)
            right_diagnol = mat[i][j] + rec_max(i + 1, j + 1)
            return max(down, left_diagnol, right_diagnol)

        out = 0
        for i in range(col):
            cur = rec_max(0, i)
            out = max(out, cur)
        return out