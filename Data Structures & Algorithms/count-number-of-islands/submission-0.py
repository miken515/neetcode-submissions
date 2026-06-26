# Count Number Of Islands Solution
#
# This solution implements an efficient algorithm for the count number of islands problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Solves the Count Number Of Islands problem.

        Algorithm: Queue-based
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - depends on problem constraints
        Space Complexity: O(n) - minimal extra space used
        """
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:  # Iterate until condition fails
                row, col = q.popleft()
                for directRow, directCol in directions:  # Iterate through collection
                    nextrow = directRow + row
                    nextcol = directCol + col

                    if (nextrow < 0 or nextcol < 0 or nextrow >= ROWS or
                        nextcol >= COLS or grid[nextrow][nextcol] == "0"
                    ):
                        continue

                    q.append((nextrow, nextcol))
                    grid[nextrow][nextcol] = "0"
        
        for r in range(ROWS):  # Process each element
            for c in range(COLS):  # Process each element
                if grid[r][c] == "1":

                    bfs(r, c)
                    islands += 1
        
        return islands