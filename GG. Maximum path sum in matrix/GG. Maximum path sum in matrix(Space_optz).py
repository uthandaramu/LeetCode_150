class Solution:
    def maximumPath(self, mat):
        # code here
        row = len(mat)
        col = len(mat[0])

        def rec_max(i, j):
            prev_arr = [0 for _ in range(col)]
            prev_arr = mat[-1][:]
            for i in range(row - 2, -1, -1):
                cur_arr = [0 for _ in range(col)]
                for j in range(col):
                    up = mat[i][j] + prev_arr[j]
                    left_diagnol = (mat[i][j] + prev_arr[j - 1]) if (j - 1 >= 0) else 0
                    right_diagnol = (mat[i][j] + prev_arr[j + 1]) if (j + 1 <= col - 1) else 0
                    cur_arr[j] = max(up, left_diagnol, right_diagnol)
                prev_arr = cur_arr
            return max(prev_arr)

        out = 0
        for i in range(col):
            cur = rec_max(row - 1, i)
            out = max(out, cur)
        return out