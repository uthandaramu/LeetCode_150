"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution(object):
    # Check if it is a valid Grid
    def isValidGrid(self, row_id, col_id, n):
        val = self.grid[row_id][col_id]

        for i in range(row_id, row_id + n):
            for j in range(col_id, col_id + n):
                if self.grid[i][j] != val:
                    return False

        return True

    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        self.grid = grid
        row = col = n = len(grid)

        row_id, col_id = 0, 0

        def rec_grid(row_id, col_id, n):

            if n == 1:
                val = True if self.grid[row_id][col_id] else False
                return Node(val, True)

            if self.isValidGrid(row_id, col_id, n):
                val = True if self.grid[row_id][col_id] else False
                node = Node(val, True)
                return node

            else:
                node = Node(True)

                # Top Left
                node.topLeft = rec_grid(row_id, col_id, n // 2)

                # Top Right
                node.topRight = rec_grid(row_id, col_id + n // 2, n // 2)

                # Bottom Left
                node.bottomLeft = rec_grid(row_id + n // 2, col_id, n // 2)

                # Bottom Right
                node.bottomRight = rec_grid(row_id + n // 2, col_id + n // 2, n // 2)

            return node

        x = rec_grid(0, 0, n)
        return x