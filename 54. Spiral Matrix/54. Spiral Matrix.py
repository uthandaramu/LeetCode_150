class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        col = len(matrix[0])

        # Right -> Bottom -> Left -> Up

        left = 0
        top = 0
        right = col - 1
        bottom = row - 1

        out = []

        while left <= right and top <= bottom:
            # Printing right
            for i in range(left, right + 1):
                out.append(matrix[top][i])

            top += 1

            # Printing Bottom
            for i in range(top, bottom + 1):
                out.append(matrix[i][right])

            right -= 1
            if top <= bottom:
                # Printing Left
                for i in range(right, left - 1, -1):
                    out.append(matrix[bottom][i])

                bottom -= 1

            if right >= left:
                # Printing Up
                for i in range(bottom, top - 1, -1):
                    out.append(matrix[i][left])

                left += 1

        return (out)