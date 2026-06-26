# Count Paths Solution
#
# This solution implements an efficient algorithm for the count paths problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Solves the Count Paths problem.

        Algorithm: Algorithm
        - Approach: Implement algorithm efficiently
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n^2) - nested loops over input
        Space Complexity: O(1) to O(n) - minimal extra space used
        """
        row = [1] * n

        for i in range(m - 1):  # Process each element
            newRow = [1] * n
            for j in range(n - 2, -1, -1):  # Process each element
                newRow[j] = newRow[j + 1] + row[j] 
            row = newRow
        
        return row[0]
