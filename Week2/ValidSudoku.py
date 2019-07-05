class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time - O(1) As the size of the board is fixed.
        # Space - O(1) As the size of the board is fixed.
        for row in board:  # Checking each row
            seen = set()
            for num in row:
                if num == '.':
                    continue
                if num in seen:
                    return False
                else:
                    seen.add(num)

        for j in range(9):  # Checking each column
            seen = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        rows = 3
        while rows < 10:  # Checking each sub 3x3 matirx.
            cols = 3
            while cols < 10:
                seen = set()
                for i in range(rows - 3, rows):
                    for j in range(cols - 3, cols):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in seen:
                            print((i, j))
                            return False
                        else:
                            seen.add(board[i][j])
                cols += 3
            rows += 3
        return True
