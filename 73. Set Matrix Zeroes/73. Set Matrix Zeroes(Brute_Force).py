class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        row_arr = [0 for _ in range(row)]
        col_arr = [0 for _ in range(col)]

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_arr[i] = 1
                    col_arr[j] = 1

        for i in range(row):
            for j in range(col):
                if (row_arr[i] == 1 or col_arr[j] == 1):
                    matrix[i][j] = 0
