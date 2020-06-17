class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board:
            m, n = len(board), len(board[0])

            def check(board, i, j):
                """
                Checks for 'O' that are connected to the 'O's on the border and
                changes all connected Os to P.
                """
                if (i >= 0 and i < m) and (j >= 0 and j < n) and board[i][j] == "O":
                    board[i][j] = "P"
                    check(board, i + 1, j)
                    check(board, i - 1, j)
                    check(board, i, j + 1)
                    check(board, i, j - 1)

            for i in range(m):
                for j in range(n):
                    if board[i][j] == "O" and (
                        i == 0 or j == 0 or i == m - 1 or j == n - 1
                    ):  # check for O on borders
                        check(board, i, j)

            for i in range(m):
                for j in range(n):
                    if board[i][j] == "O":
                        board[i][j] = "X"
                    elif board[i][j] == "P":
                        board[i][j] = "O"
