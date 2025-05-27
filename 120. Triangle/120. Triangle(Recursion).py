class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        col = len(triangle[-1])

        def recur_tri(i, j):
            if i == row - 1:
                return triangle[i][j]
            down = triangle[i][j] + recur_tri(i + 1, j)
            diagnol = triangle[i][j] + recur_tri(i + 1, j + 1)
            return min(down, diagnol)

        return (recur_tri(0, 0))