class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time - O(n^2) ; n is number of characters in the board
        # Space - O(n) For the recursive call stack
        # Apply DFS on every character in the board.
        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = set()
                if self.DFS((i, j), board, word, seen, 0):
                    return True
        return False

    def DFS(self, start, board, word, seen, position):
        # position tracks the word index where we are checking for.
        # If position is greater than or equal to length of word means we found the word already.
        if position >= len(word):
            return True
        r, c = start
        if board[r][c] != word[position]:
            # check if the current character in the board mathces with the corresponding character in the word.
            return False
        if start in seen:
            # If the the current element was already used before, we cannot use it again.
            return False
        seen.add(start)  # if we are using it to construct the word, we add it to seen hashset.
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]  # Neighbours
        for i, j in directions:
            if r + i >= 0 and r + i < len(board) and c + j >= 0 and c + j < len(board[0]):
                if self.DFS((r + i, c + j), board, word, seen, position + 1):
                    return True
        # If the element cannot be a part of the word, remove it from the hashset
        seen.remove(start)
        return False