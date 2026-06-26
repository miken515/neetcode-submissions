# Search For Word Solution
#
# This solution implements an efficient algorithm for the search for word problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Solves the Search For Word problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board [r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'

            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            board[r][c] = word[i]
            return res

        
        for r in range(ROWS):  # Process each element
            for c in range(COLS):  # Process each element
                if dfs(r, c, 0):
                    return True
        return False