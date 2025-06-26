class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        n = 3
        [0][0] -> [0][2]
        [0][1] -> [1][2]
        [0][2] -> [2][2]
        [1][0] -> [0][1]
        [1][1] -> [1][1]
        [r][c] -> [c][(n-1)-r]
        """

        n = len(matrix)

        out = [[0 for _ in range(n)] for _ in range(n)]

        for r in range(n):
            for c in range(n):
                out[c][(n - 1) - r] = matrix[r][c]

        print(out)