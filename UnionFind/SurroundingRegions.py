from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Time - O(m*n)
        # Space - O(m*n)

        if len(board) == 0:
            return
        nrow = len(board)
        ncol = len(board[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        bounds = set()
        # putting all boundary positions into a set using 2 for loops.
        for i in [0, nrow - 1]:
            for j in range(ncol):
                bounds.add((i, j))
        for i in [0, ncol - 1]:
            for j in range(nrow):
                bounds.add((j, i))
        # Graph BFS starts here.
        for i, j in bounds:  # From each bound we we traverse and mark which will not be flipped as 'K'
            if board[i][j] == "O":
                queue = deque()
                queue.append((i, j))
                while queue:
                    i, j = queue.popleft()
                    if (i, j) in visited:
                        continue
                    board[i][j] = 'K'
                    visited.add((i, j))
                    for a, b in directions:
                        if not (i + a <= 0 or i + a >= nrow - 1 or j + b <= 0 or j + b >= ncol - 1):
                            if board[i + a][j + b] == 'O':
                                queue.append((i + a, j + b))
        # Loop through all the elements and flip all the 'O's to 'X' and 'K's to 'O'.
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == 'K':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'