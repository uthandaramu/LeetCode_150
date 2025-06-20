class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        visited = [[0 for _ in range(col)] for _ in range(row)]

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            if board[r][c] == "O" and visited[r][c] == 0:
                visited[r][c] = 1
                dfs(r, c + 1)
                dfs(r, c - 1)
                dfs(r - 1, c)
                dfs(r + 1, c)
            else:
                return

        for c in range(col):
            dfs(0, c)
            dfs(row - 1, c)

        for r in range(row):
            dfs(r, 0)
            dfs(r, col - 1)

        for i in range(row):
            for j in range(col):
                if visited[i][j] == 0:
                    board[i][j] = "X"