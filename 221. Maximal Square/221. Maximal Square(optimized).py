class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        dp_arr = [[0 for _ in range(col)] for _ in range(row)]
        maxi = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp_arr[i][j] = 1
                    else:
                        dp_arr[i][j] = min(
                            dp_arr[i-1][j],        # top
                            dp_arr[i][j-1],        # left
                            dp_arr[i-1][j-1]       # top-left
                        ) + 1
                    maxi = max(maxi, dp_arr[i][j])

        return maxi * maxi