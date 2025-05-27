class Solution:
    def maximumPath(self, mat):
        # code here
        row = len(mat)
        col = len(mat[0])

        dp_arr = [[0 for _ in range(col)] for _ in range(row)]
        dp_arr[-1] = mat[-1][:]

        def rec_max(i, j):
            for i in range(row - 2, -1, -1):
                for j in range(col):
                    up = mat[i][j] + dp_arr[i + 1][j]
                    left_diagnol = (mat[i][j] + dp_arr[i + 1][j - 1]) if (j - 1 >= 0) else 0
                    right_diagnol = (mat[i][j] + dp_arr[i + 1][j + 1]) if (j + 1 <= col - 1) else 0
                    dp_arr[i][j] = max(up, left_diagnol, right_diagnol)
            return max(dp_arr[0])

        out = 0
        for i in range(col):
            cur = rec_max(row - 1, i)
            out = max(out, cur)
        return out