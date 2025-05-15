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
        dp_arr[-1] = triangle[-1]
        for i in range(row - 2, -1, -1):
            for j in range(i, -1, -1):
                up = triangle[i][j] + dp_arr[i + 1][j]
                diagnol = triangle[i][j] + dp_arr[i + 1][j + 1]
                dp_arr[i][j] = min(up, diagnol)

        return (dp_arr[0][0])