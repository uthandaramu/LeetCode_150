class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        orgMatrix ---> Transpose ---> reverse elements in the row ----> output
        """

        n = len(matrix)

        # Transpose
        # for transpose diagnal elements([0][0], [1][1], ..) will be in same place
        # we need to swap only upper triangle
        """
        n = 4
        [0][1] - > [1][0]  |  [1][2] - > [2][1]  |  [2][3] - > [3][2]
        [0][2] - > [2][0]  |  [1][3] - > [3][1]  |
        [0][3] - > [3][0]  |                     |

        [0 to (n-2)][(r+1) to (n-1)] - > swap
        """

        for r in range(n - 1):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Reverse the elements in each row:
        for r in range(n):
            matrix[r].reverse()