# Rotting Fruit Solution
#
# This solution implements an efficient algorithm for the rotting fruit problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Solves the Rotting Fruit problem.

        Algorithm: Queue-based
        - Approach: Implement algorithm efficiently
        - Key Operations: insert nodes/elements into result structure

        Time Complexity: O(n) - depends on problem constraints
        Space Complexity: O(n) - minimal extra space used
        """
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):  # Process each element
            for c in range(COLS):  # Process each element
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        print(fresh)
        while q and fresh > 0:  # Iterate until condition fails
            for i in range(len(q)):  # Process each element
                r, c = q.popleft()

                for dr, dc in directions:  # Iterate through collection
                    row, col = dr + r, dc + c
                    if (row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] != 1):
                        continue

                    print(grid[row][col])
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1