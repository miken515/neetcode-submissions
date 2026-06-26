# Longest Common Subsequence Solution
#
# This solution implements an efficient algorithm for the longest common subsequence problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Solves the Longest Common Subsequence problem.

        Algorithm: Dynamic Programming
        - Approach: Build solution bottom-up using subproblems
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n) - compute each subproblem once
        Space Complexity: O(n) - store results for each subproblem
        """
        grid = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):  # Process each element
            for j in range(len(text2) - 1, -1, -1):  # Process each element
                if text1[i] == text2[j]: 
                    grid[i][j] = 1 + grid[i + 1][j + 1] # adding 1 and diagonal
                else:
                    grid[i][j] = max(grid[i][j+1], grid[i + 1][j]) #max to the right or bottom
        
        return grid[0][0]

# DP algo
# Create a 2d grid to all zeros
# starting bottom right of 2d matrix