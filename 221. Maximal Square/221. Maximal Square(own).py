class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        col = len(matrix[0])
        row = len(matrix)
        dp_arr = [[0 for _ in range(col)] for _ in range(row)]

        maxi = 0

        for i in range(row):
            for j in range(col):
                if i == 0:
                    dp_arr[i][j] = int(matrix[i][j])
                if j == 0:
                    dp_arr[i][j] = int(matrix[i][j])
                if (i - 1) >= 0 and (j - 1) >= 0:
                    if int(matrix[i][j]) == 1 and dp_arr[i][j - 1] > 0 and dp_arr[i - 1][j] > 0 and dp_arr[i - 1][
                        j - 1] > 0:
                        dp_arr[i][j] = min(dp_arr[i][j - 1], dp_arr[i - 1][j], dp_arr[i - 1][j - 1]) + 1
                    else:
                        dp_arr[i][j] = int(matrix[i][j])
                maxi = max(maxi, dp_arr[i][j])

        return (maxi * maxi)