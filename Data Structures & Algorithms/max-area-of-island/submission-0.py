# Max Area Of Island Solution
#
# This solution implements an efficient algorithm for the max area of island problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Solves the Max Area Of Island problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0 or
                r == ROWS or
                c < 0 or 
                c == COLS or 
                grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0
            
            visit.add((r, c))

            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
            
        res = 0
        for r in range(ROWS):  # Process each element
            for c in range(COLS):  # Process each element
                res = max(res, dfs(r, c))

        return res
        
