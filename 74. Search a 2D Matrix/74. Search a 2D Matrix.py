class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        visited = set()

        row = len(matrix)
        col = len(matrix[0])

        start, end = 0, (row * col) - 1

        while start <= end:

            mid = (start + end) // 2
            i = mid // col
            j = mid % col

            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                start = mid + 1
            else:
                end = mid - 1

        return False