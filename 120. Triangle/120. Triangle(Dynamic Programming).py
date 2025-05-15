import sys

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        col = len(triangle[-1])
        dp_arr = [[sys.maxint for _ in range(col)] for _ in range(row)]

        def recur_tri(i, j):
            if i == row - 1:
                return triangle[i][j]
            if dp_arr[i][j] == sys.maxint:
                down = triangle[i][j] + recur_tri(i + 1, j)
                diagnol = triangle[i][j] + recur_tri(i + 1, j + 1)
                dp_arr[i][j] = min(down, diagnol)
            return dp_arr[i][j]

        return (recur_tri(0, 0))