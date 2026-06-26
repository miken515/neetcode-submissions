# Counting Bits Solution
#
# This solution implements an efficient algorithm for the counting bits problem.
# Key concepts: Analyze constraints, choose optimal data structures, handle edge cases
#
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Solves the Counting Bits problem.

        Algorithm: Dynamic Programming
        - Approach: Build solution bottom-up using subproblems
        - Key Operations: recursive exploration with memoization

        Time Complexity: O(n) - compute each subproblem once
        Space Complexity: O(n) - store results for each subproblem
        """
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):  # Process each element
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp